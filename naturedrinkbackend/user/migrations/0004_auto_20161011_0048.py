# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_address_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]