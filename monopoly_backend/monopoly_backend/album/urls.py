from django.urls import path
from .views import AlbumListCreateView, AlbumDetailView

urlpatterns = [
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail')
]
