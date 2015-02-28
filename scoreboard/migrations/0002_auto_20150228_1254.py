# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last_loss',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='last_win',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
