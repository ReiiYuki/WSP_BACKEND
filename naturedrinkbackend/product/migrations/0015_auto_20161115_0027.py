# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20161115_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='design',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='design.DesignBottle'),
        ),
    ]
