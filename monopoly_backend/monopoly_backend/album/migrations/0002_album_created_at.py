# Generated by Django 4.2.9 on 2024-01-24 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
