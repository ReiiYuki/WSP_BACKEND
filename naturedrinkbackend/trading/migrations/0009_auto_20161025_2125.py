# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0008_order_postal_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pay_date',
            new_name='last_update_date',
        ),
    ]