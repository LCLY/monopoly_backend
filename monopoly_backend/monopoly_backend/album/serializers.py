from rest_framework import serializers
from .models import Album
from sticker.serializers import StickerSerializer


class AlbumSerializer(serializers.ModelSerializer):
    sticker = StickerSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
