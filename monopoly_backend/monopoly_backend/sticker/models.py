from django.db import models
from django.utils import timezone
from album.models import Album
from django.db.models import Q
# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL


class StickerQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(name__icontains=query) | Q(rarity__icontains=query)
        return self.filter(lookups)


class StickerManager(models.Manager):
    def get_queryset(self):
        return StickerQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Sticker(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    rarity = models.IntegerField()
    # add foreign key of album and when album is deleted all stickers should be deleted as well
    album = models.ForeignKey(
        Album, null=True, on_delete=models.CASCADE, related_name='stickers')
    objects = StickerManager()
    user = models.ManyToManyField(User, through="StickerUser")

    def __str__(self):
        return self.name


class StickerUserQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(count__icontains=query)
        return self.filter(lookups)


class StickerUserManager(models.Manager):
    def get_queryset(self):
        return StickerUserQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class StickerUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    objects = StickerManager()
