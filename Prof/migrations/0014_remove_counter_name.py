# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 03:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prof', '0013_counter_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counter',
            name='name',
        ),
    ]