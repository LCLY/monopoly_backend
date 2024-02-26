from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.
from season.models import Season


class Album(models.Model):
    name = models.CharField(max_length=220)
    # if delete season, album will disappear
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, null=True, blank=True, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
