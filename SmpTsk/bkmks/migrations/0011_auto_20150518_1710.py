# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0010_auto_20150518_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created', editable=False),
        ),
    ]
