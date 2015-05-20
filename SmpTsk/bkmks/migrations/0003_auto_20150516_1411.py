# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0002_taskitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskitem',
            old_name='task_n',
            new_name='taskn',
        ),
        migrations.RenameField(
            model_name='taskitem',
            old_name='user_n',
            new_name='usern',
        ),
    ]
