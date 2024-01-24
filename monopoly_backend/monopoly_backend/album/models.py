from django.db import models
from sticker.models import Sticker
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=255)


# add foreign key of sticker
sticker = models.ForeignKey(
    Sticker, on_delete=models.SET_NULL, null=True, related_name='album')
