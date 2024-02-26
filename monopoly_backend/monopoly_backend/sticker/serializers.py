from rest_framework import serializers
from .models import Sticker, StickerUser


class StickerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sticker
        fields = ['id', 'album', 'name', 'rarity', 'image_url', 'created_at']


class StickerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = StickerUser
        fields = "__all__"
