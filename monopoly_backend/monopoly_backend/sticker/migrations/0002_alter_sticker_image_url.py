# Generated by Django 4.2.9 on 2024-01-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sticker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]