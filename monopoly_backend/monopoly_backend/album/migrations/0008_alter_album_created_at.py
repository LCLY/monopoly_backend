# Generated by Django 4.2.9 on 2024-02-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_delete_albumsticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]