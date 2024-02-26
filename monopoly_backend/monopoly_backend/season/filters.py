from django_filters.rest_framework import DateFromToRangeFilter
from django_filters import rest_framework as djfilters
from django.utils import timezone


class SeasonFilter(djfilters.FilterSet):
    name = djfilters.CharFilter(field_name='name', lookup_expr='icontains')
    # date_from = djfilters.DateFilter(field_name='date_from')
    # date_to = djfilters.DateFilter(field_name='date_to')
    date_to_range = DateFromToRangeFilter(field_name='date_to')
    date_from_range = DateFromToRangeFilter(field_name='date_from')
    current_season = djfilters.BooleanFilter(
        method='filter_current_season', label='Is Current Season')

    def filter_current_season(self, queryset, name, value):
        qs = queryset
        current_date = timezone.now()

        if value == True:
            qs = qs.filter(date_to__gte=current_date,
                           date_from__lte=current_date)
        else:
            qs = qs.exclude(date_to__gte=current_date,
                            date_from__lte=current_date)
        return qs
