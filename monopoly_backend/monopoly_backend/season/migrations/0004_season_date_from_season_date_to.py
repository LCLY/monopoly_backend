# Generated by Django 4.2.9 on 2024-02-06 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_alter_season_created_at_alter_season_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='date_from',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='season',
            name='date_to',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
