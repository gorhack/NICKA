# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0003_auto_20150930_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 9, 30), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 9, 30)),
            preserve_default=False,
        ),
    ]
