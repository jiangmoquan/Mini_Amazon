# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20150324_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='power',
            new_name='Fashion_element',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='wireless_type',
            new_name='Picture',
        ),
        migrations.RemoveField(
            model_name='product',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cpu_model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='eth_chip',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_usb',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lan_ports',
        ),
        migrations.RemoveField(
            model_name='product',
            name='lan_speed',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wan_ports',
        ),
        migrations.AddField(
            model_name='product',
            name='Chest',
            field=models.IntegerField(verbose_name='Chest', default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='Has_waitband',
            field=models.BooleanField(verbose_name='Has waistband', default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Material',
            field=models.CharField(max_length=127, blank=True, verbose_name='Material'),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_num',
            field=models.FloatField(editable=False, default=0, verbose_name='Product number'),
        ),
        migrations.AddField(
            model_name='product',
            name='Shoulder',
            field=models.IntegerField(verbose_name='Shoulder', default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='product',
            name='Style',
            field=models.CharField(max_length=127, blank=True, verbose_name='Style'),
        ),
        migrations.AddField(
            model_name='product',
            name='Waist',
            field=models.IntegerField(verbose_name='Waist', default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
