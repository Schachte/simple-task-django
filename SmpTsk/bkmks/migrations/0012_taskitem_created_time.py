# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0011_auto_20150518_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='created_time',
            field=models.TimeField(default=datetime.datetime(2015, 5, 19, 0, 41, 0, 298685, tzinfo=utc), verbose_name=b'time created', auto_now_add=True),
            preserve_default=False,
        ),
    ]
