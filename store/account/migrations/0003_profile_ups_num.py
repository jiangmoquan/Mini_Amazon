# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150128_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ups_num',
            field=models.IntegerField(default=0, verbose_name='ups number'),
        ),
    ]
