from django.contrib import admin
from models import *

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ('winner', 'loser', 'points','date')
admin.site.register(Game, GameAdmin)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
admin.site.register(Player, PlayerAdmin)
