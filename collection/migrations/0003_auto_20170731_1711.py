# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('collection', '0002_auto_20170731_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('song_lyrics', 'liad'), ('tongue_twister', 'zunga breha'), ('saying', 'šbruh'), ('poem', 'gedihd'), ('story', 'gšihd'), ('help', 'huif')], max_length=50)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_items', to='user.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCollection',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('creation_date', models.DateField(blank=True, editable=False)),
                ('type', models.CharField(choices=[('song_lyrics', 'liad'), ('tongue_twister', 'zunga breha'), ('saying', 'šbruh'), ('poem', 'gedihd'), ('story', 'gšihd'), ('help', 'huif')], max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.Profile')),
            ],
            options={
                'verbose_name': 'historical collection',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.RemoveField(
            model_name='collectionitem',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='CollectionItem',
        ),
    ]
