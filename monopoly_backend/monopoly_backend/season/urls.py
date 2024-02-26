from django.urls import path
from .views import SeasonListCreateView, SeasonDetailView

urlpatterns = [
    path('seasons/', SeasonListCreateView.as_view(), name='season-list'),
    path('seasons/<int:pk>/', SeasonDetailView.as_view(), name='season-detail'),
]
