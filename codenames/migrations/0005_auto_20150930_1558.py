# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0004_auto_20150930_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='repeating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='operation',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
