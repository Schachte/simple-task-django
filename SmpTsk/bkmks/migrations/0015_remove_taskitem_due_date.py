# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0014_auto_20150519_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskitem',
            name='due_date',
        ),
    ]
