from django.shortcuts import render
from rest_framework import generics
from .models import Sticker, StickerUser
from .serializers import StickerSerializer, StickerUserSerializer
from django_filters import rest_framework as filters
from config.mixins import UserQuerysetMixin
# Create your views here.


class StickerListCreateView(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('rarity', "name")


class StickerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer


class StickerUserListCreateView(UserQuerysetMixin, generics.ListCreateAPIView):
    queryset = StickerUser.objects.all()
    serializer_class = StickerUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('count',)
