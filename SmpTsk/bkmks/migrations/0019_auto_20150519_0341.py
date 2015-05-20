# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0018_auto_20150519_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.CharField(default=b'Enter', max_length=20),
        ),
    ]
