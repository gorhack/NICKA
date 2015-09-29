# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=7),
        ),
    ]
