# Generated by Django 4.2.9 on 2024-02-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0005_remove_season_current_season'),
        ('album', '0009_album_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='season.season'),
        ),
    ]
