# Generated by Django 3.2.9 on 2022-02-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20220211_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviestatus',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_status',
            field=models.ManyToManyField(blank=True, related_name='movies', to='api.MovieStatus'),
        ),
    ]
