# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0017_auto_20150519_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.DateField(default=datetime.date.today, max_length=20),
        ),
    ]
