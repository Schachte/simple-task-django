# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkmks', '0019_auto_20150519_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='information',
            field=models.CharField(default=b'Additional information', max_length=4000),
        ),
    ]
