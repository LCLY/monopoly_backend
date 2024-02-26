# album/admin.py
from django.contrib import admin
from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'season_name', 'total_stickers')
    raw_id_fields = ['season']

    def season_name(self, obj):
        return obj.season.name if obj.season else None

    def total_stickers(self, obj):
        return obj.stickers.count()


admin.site.register(Album, AlbumAdmin)
