# Generated by Django 3.2.9 on 2022-02-12 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_profile_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='movies',
        ),
    ]