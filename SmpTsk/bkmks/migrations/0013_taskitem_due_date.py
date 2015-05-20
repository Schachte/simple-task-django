# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0012_taskitem_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='due_date',
            field=models.CharField(default=b'date', max_length=20),
        ),
    ]
