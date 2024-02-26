from rest_framework import serializers
from .models import Album
from sticker.models import Sticker
from sticker.serializers import StickerSerializer


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'name', 'season', "stickers"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET']:
                self.fields['stickers'] = StickerSerializer(
                    many=True, read_only=True)

        except:
            pass
