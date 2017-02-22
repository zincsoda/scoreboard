from scoreboard.models import Player, Game

import math;

class Scoring(object):

    def k_factor(self):
        return 30

    def get_expectation(self,rating_1, rating_2):
        calc = (1.0 / (1.0 + pow(10, (float(rating_2 - rating_1) / 400))));
        return calc;

    def get_delta(self, rating, expected, actual):
        calc = (self.k_factor() * (actual - expected));
        return calc

    def modify_rating(self, rating, expected, actual):
        calc = (rating + self.k_factor() * (actual - expected));
        return calc;
    
    def update_player_ratings(self, winner, loser):
        winner_expected = self.get_expectation(winner.rating, loser.rating)
        print 'winner_expected: ', winner_expected
        loser_expected = winner_expected
        print 'loser_expected: ',loser_expected
        points = self.get_delta(winner.rating, winner_expected, 1.0)
        print 'points: ', points
        winner.rating = self.modify_rating(winner.rating, winner_expected, 1.0)
        loser.rating = self.modify_rating(loser.rating, loser_expected, 0)
        winner.save()
        loser.save()
        return points

    def update_player_streak(self, winner, loser):
        if winner.streak < 0:
            winner.streak = 1
        else:
            winner.streak += 1

        if loser.streak > 0:
            loser.streak = -1
        else:
            loser.streak -= 1
        winner.save()
        loser.save()

    def reset_ratings(self):
        for player in Player.objects.all():
            player.rating = 2000
            player.streak = 0
            player.save()

    def recalculate_scores(self):
        self.reset_ratings()
        for game in Game.objects.all():
            self.update_player_streak(game.winner, game.loser)
            self.update_player_ratings(game.winner, game.loser) 
            game.save()
