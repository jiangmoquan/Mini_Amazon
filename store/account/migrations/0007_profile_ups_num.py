# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profile_ups_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ups_num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
