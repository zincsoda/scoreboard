from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from scoreboard.models import Player, Game
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from scoreboard.scoring import Scoring
import math;

def home(request):
    last_game = Game.objects.all().last()
    players = Player.objects.order_by('rating').reverse()
    players_last_win_loss = []
    number_of_games = Game.objects.all().count()

    resp_dict = {"players": players, "last_game":last_game, "number_of_games":number_of_games}
    return render_to_response('home.html', resp_dict, context_instance=RequestContext(request))


@csrf_protect
def add_score(request):
    if request.method =="POST":

        winner = Player.objects.get(name=request.POST.get('winner'))
        loser = Player.objects.get(name=request.POST.get('loser'))
        if winner == loser:
            print "Error: can't have a player playing him/herself"
            return HttpResponseRedirect('/')

        delta = Scoring().update_player_ratings(winner, loser)
        Scoring().update_player_streak(winner, loser)

        winner.last_win = loser.name
        loser.last_loss = winner.name
        winner.save()
        loser.save()

        new_game = Game.objects.create(winner=winner, loser=loser, points=delta)
        new_game.save()
    else:
        print request.method
        print request.META["CONTENT_TYPE"]

    return HttpResponseRedirect('/')
