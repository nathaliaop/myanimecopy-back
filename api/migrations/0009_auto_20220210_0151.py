# Generated by Django 3.2.9 on 2022-02-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220210_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='episode',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='season',
            name='number',
            field=models.IntegerField(),
        ),
    ]
