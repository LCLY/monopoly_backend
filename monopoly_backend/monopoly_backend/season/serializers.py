from rest_framework import serializers
from .models import Season
from album.serializers import AlbumSerializer


class SeasonSerializer(serializers.ModelSerializer):
    current_season = serializers.BooleanField(
        read_only=True)

    class Meta:
        model = Season
        fields = ['id', 'name',
                  'date_from', 'date_to', 'current_season', 'albums']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['GET']:
                self.fields['albums'] = AlbumSerializer(
                    many=True, read_only=True)
        except:
            pass
