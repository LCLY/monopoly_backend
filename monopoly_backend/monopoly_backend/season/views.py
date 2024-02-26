from django.shortcuts import render
from rest_framework import generics, filters
from .models import Season
from .serializers import SeasonSerializer
from .filters import SeasonFilter
from django_filters.rest_framework import DjangoFilterBackend

# from django_filters import rest_framework as filters

# Create your views here.
from django.utils import timezone
from django.db.models import Count, Case, When, IntegerField


class SeasonListCreateView(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_class = SeasonFilter
    # Specify fields for ordering
    ordering_fields = ['name', 'date_from', 'date_to']
    ordering = ['-date_from']

    def get_queryset(self):
        qs = super().get_queryset()
        # newest = Comment.objects.filter(post=OuterRef("pk")).order_by("-created_at")
        current_time = timezone.now()

        # by using annotation, we add custom conditional expression to the qs
        # this is used when we need to add extra info without altering the data in db

        # here we are creating a new field called current_season, check if current time is within date_from and date_to, set value to 1, count it and in serializers because we set to boolean, if value is 0, it will be false
        # Count is counting the occurences of non-null values, not the actual value itself
        qs = qs.annotate(current_season=Count(Case(
            When(date_from__lte=current_time,
                 date_to__gte=current_time, then=1),
            output_field=IntegerField(),
        )))
        return qs


class SeasonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
