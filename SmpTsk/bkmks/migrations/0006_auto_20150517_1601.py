# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0005_auto_20150517_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='taskn',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='usern',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
