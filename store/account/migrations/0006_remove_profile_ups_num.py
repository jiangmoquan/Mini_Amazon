# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180426_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ups_num',
        ),
    ]
