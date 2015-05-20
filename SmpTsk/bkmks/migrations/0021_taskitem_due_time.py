# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0020_taskitem_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='due_time',
            field=models.CharField(default=b'Enter', max_length=20),
        ),
    ]
