# Generated by Django 4.2.9 on 2024-02-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0004_alter_sticker_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='rarity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]