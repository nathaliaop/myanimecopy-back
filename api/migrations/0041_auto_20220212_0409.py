# Generated by Django 3.2.9 on 2022-02-12 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20220212_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.anime'),
        ),
        migrations.AlterField(
            model_name='status',
            name='manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.manga'),
        ),
        migrations.AlterField(
            model_name='status',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.movie'),
        ),
        migrations.AlterField(
            model_name='status',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
        ),
    ]
