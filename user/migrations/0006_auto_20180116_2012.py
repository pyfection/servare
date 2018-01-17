# Generated by Django 2.0.1 on 2018-01-16 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userlanguage_is_moderator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlanguage',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_languages', to='language.Language'),
        ),
    ]