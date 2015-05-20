# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0022_auto_20150519_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='due_time',
            field=models.CharField(default=b'None', max_length=20),
        ),
    ]
