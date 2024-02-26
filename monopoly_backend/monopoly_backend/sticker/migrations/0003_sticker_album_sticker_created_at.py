# Generated by Django 4.2.9 on 2024-01-24 04:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_created_at'),
        ('sticker', '0002_alter_sticker_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.album'),
        ),
        migrations.AddField(
            model_name='sticker',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
