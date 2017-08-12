# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
        ('word', '0012_auto_20170812_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalword',
            name='language',
        ),
        migrations.RemoveField(
            model_name='word',
            name='language',
        ),
        migrations.AddField(
            model_name='wordversion',
            name='language',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='language.Language'),
            preserve_default=False,
        ),
    ]
