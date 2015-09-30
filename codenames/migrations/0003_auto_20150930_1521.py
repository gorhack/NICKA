# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenames', '0002_auto_20150930_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='clearance',
            field=models.CharField(default=b'UNC', max_length=3, choices=[(b'UNC', b'UNCLASSIFIED'), (b'SEC', b'SECRET'), (b'TSI', b'TOP SECRET')]),
        ),
    ]
