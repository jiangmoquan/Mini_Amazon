# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180426_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truck',
            old_name='truck_count',
            new_name='truck_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='tracking_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='truck_id',
            field=models.IntegerField(null=True),
        ),
    ]
