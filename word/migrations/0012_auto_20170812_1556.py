# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0011_auto_20170812_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalword',
            name='ipa',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='word',
            name='ipa',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
