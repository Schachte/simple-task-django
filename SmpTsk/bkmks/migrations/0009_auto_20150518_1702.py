# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0008_taskitem_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
