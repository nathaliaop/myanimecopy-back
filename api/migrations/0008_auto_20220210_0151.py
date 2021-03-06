# Generated by Django 3.2.9 on 2022-02-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_anime_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='number',
            field=models.IntegerField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='season',
            name='number',
            field=models.IntegerField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
