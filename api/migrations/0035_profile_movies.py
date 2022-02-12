# Generated by Django 3.2.9 on 2022-02-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_remove_profile_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='movies',
            field=models.ManyToManyField(through='api.Status', to='api.Movie'),
        ),
    ]
