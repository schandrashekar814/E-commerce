# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-17 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',

        ),
    ]
