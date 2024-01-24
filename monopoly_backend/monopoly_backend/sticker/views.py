from django.shortcuts import render
from rest_framework import generics
from .models import Sticker
from .serializers import StickerSerializer

# Create your views here.


class StickerListCreateView(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer


class StickerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
