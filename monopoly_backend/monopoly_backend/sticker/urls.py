from django.urls import path
from .views import StickerListCreateView, StickerDetailView, StickerUserListCreateView

urlpatterns = [
    path('stickers/', StickerListCreateView.as_view(), name='sticker-list'),
    path('stickers/<int:pk>/', StickerDetailView.as_view(), name='sticker-detail'),
    path('user_stickers/', StickerUserListCreateView.as_view(),
         name='sticker-user-list'),
]
