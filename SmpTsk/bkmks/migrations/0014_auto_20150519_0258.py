# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0013_taskitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='due_date',
            field=models.CharField(max_length=20),
        ),
    ]
