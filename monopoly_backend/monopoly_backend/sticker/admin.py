from django.contrib import admin
from .models import Sticker, StickerUser

# Register your models here.


class StickerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "rarity", "album"]


admin.site.register(Sticker, StickerAdmin)


class StickerUserAdmin(admin.ModelAdmin):
    list_display = ["user", "sticker", "count",]


admin.site.register(StickerUser, StickerUserAdmin)
