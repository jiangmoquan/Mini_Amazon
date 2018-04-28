# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20180428_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=1, default='P', choices=[('P', 'Pending'), ('K', 'Packaging'), ('T', 'Ready to load'), ('L', 'Loading'), ('D', 'Loaded'), ('S', 'Shipping'), ('E', 'Delivered'), ('R', 'Received'), ('H', 'Wait for Buying'), ('C', 'Cancelled')]),
        ),
    ]
