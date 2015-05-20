# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0023_auto_20150519_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created', editable=False),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='created_time',
            field=models.TimeField(verbose_name='time created', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='due_time',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='information',
            field=models.CharField(default='Additional information', max_length=4000),
        ),
    ]
