# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20150324_2315'),
        ('order', '0004_order_close_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('open_quantity', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('truck_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('location_x', models.IntegerField(default=0)),
                ('location_y', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_y',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_num',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='P', choices=[('P', 'Pending'), ('K', 'Packaging'), ('T', 'Ready to load'), ('L', 'Loading'), ('D', 'Loaded'), ('S', 'Shipping'), ('E', 'Delivered'), ('R', 'Received'), ('H', 'Hold'), ('C', 'Cancelled')], max_length=1),
        ),
        migrations.AddField(
            model_name='truck',
            name='wh_id',
            field=models.ForeignKey(to='order.Warehouse'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='wh_id',
            field=models.ForeignKey(to='order.Warehouse'),
        ),
        migrations.AddField(
            model_name='order',
            name='truck_id',
            field=models.ForeignKey(to='order.Truck', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='wh_id',
            field=models.ForeignKey(to='order.Warehouse', null=True),
        ),
    ]
