# Generated by Django 3.2.9 on 2022-02-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20220210_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='following',
            field=models.ManyToManyField(related_name='following', to='api.Profile'),
        ),
    ]
