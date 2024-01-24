from django.urls import path
from .views import StickerListCreateView, StickerDetailView

urlpatterns = [
    path('stickers/', StickerListCreateView.as_view(), name='sticker-list'),
    path('stickers/<int:pk>/', StickerDetailView.as_view(), name='sticker-detail'),
]
