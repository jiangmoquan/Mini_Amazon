# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180426_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ups_num',
            field=models.IntegerField(verbose_name='ups number', null=True, blank=True),
        ),
    ]
