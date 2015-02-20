from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from scoreboard.scoring import Scoring

class Command(BaseCommand):
    args = ''
    help = 'Recalculate scores'

    def handle(self, *args, **options):
        Scoring().recalculate_scores()

