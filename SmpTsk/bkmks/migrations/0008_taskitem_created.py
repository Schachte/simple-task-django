# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0007_auto_20150518_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 0, 0, 41, 24957, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
