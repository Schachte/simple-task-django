# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0004_remove_userprofile_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='taskn',
            field=models.CharField(help_text=b'Please enter your task.', max_length=400, verbose_name=b'task'),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='usern',
            field=models.ForeignKey(related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
