# Generated by Django 4.2.9 on 2024-02-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0005_sticker_rarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]