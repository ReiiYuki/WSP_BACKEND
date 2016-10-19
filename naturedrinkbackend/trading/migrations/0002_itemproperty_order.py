# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20161019_1246'),
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductChoice')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductOption')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('pay_date', models.DateField(blank=True, default=None, null=True)),
                ('transfer_slip', models.ImageField(default=None, upload_to='images/slips')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.PaymentMethod')),
            ],
        ),
    ]
