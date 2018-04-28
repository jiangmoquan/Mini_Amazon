# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_ups_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ups_num',
            field=models.IntegerField(default=0),
        ),
    ]
