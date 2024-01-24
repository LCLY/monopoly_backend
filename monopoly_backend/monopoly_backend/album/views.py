from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer

# Create your views here.


class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
