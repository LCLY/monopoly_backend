# Generated by Django 4.2.9 on 2024-02-05 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_albumsticker_image_url_albumsticker_rarity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AlbumSticker',
        ),
    ]
