from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Player(models.Model):
    name = models.CharField(max_length=128)
    rating = models.IntegerField(default=2000)
    streak = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name

class Game(models.Model):
    date = AutoDateTimeField(default=timezone.now)

    winner = models.ForeignKey(Player, blank=True, null=True, related_name='%(class)s_game_winner')
    loser = models.ForeignKey(Player, blank=True, null=True, related_name='%(class)s_game_loser')
    points = models.IntegerField()

    def __unicode__(self):
        return '%s' % self.id


