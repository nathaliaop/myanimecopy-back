# Generated by Django 3.2.9 on 2022-02-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='profiles',
            field=models.ManyToManyField(to='api.Profile'),
        ),
        migrations.AddField(
            model_name='manga',
            name='profiles',
            field=models.ManyToManyField(to='api.Profile'),
        ),
        migrations.AddField(
            model_name='movie',
            name='profiles',
            field=models.ManyToManyField(to='api.Profile'),
        ),
    ]
