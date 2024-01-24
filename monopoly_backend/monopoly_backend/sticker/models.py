from django.db import models

# Create your models here.


class Sticker(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
