# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='clearance',
            field=models.CharField(default=b'UNC', max_length=3),
        ),
    ]
