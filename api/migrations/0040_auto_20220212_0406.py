# Generated by Django 3.2.9 on 2022-02-12 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_status_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='anime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='api.anime'),
        ),
        migrations.AlterField(
            model_name='status',
            name='manga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='api.manga'),
        ),
        migrations.AlterField(
            model_name='status',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='api.movie'),
        ),
    ]
