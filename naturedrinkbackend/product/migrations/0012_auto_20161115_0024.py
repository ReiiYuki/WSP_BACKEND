# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20161115_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='design.DesignBottle'),
        ),
    ]
