from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Album
from sticker.models import Sticker
from .serializers import AlbumSerializer
from rest_framework.exceptions import ValidationError
from sticker.serializers import StickerSerializer
from rest_framework import status
from django_filters import rest_framework as filters


# Create your views here.


class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', "season",)


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
