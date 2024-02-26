# Generated by Django 4.2.9 on 2024-02-05 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_remove_album_stickers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=220),
        ),
        migrations.CreateModel(
            name='AlbumSticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
            ],
        ),
    ]