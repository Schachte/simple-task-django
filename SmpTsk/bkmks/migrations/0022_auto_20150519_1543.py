# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0021_taskitem_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_time',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
