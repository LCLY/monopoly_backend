from django.contrib import admin
from .models import Season

# Register your models here.


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name',  'date_from', 'date_to']


admin.site.register(Season, SeasonAdmin)
