from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
# Create your models here.


class Season(models.Model):
    name = models.CharField(max_length=220)
    # current_season = models.BooleanField(default=False)
    date_from = models.DateField(default=date.today, blank=False)
    date_to = models.DateField(default=date.today, blank=False)
    created_at = CreationDateTimeField()
    updated_at = ModificationDateTimeField()

    # def clean(self):
    #     if self.current_season:
    #         # check if htere's already a current season set to True in database
    #         current_season_exists = Season.objects.filter(
    #             current_season=True).exclude(id=self.id).exists()
    #         if current_season_exists:
    #             raise ValidationError(
    #                 'There can only be one current season at a time!')
    # If this is a new season, set current_season to True for the latest one

    # def save(self, *args, **kwargs):
    #     # if the current season is being saved for the first time
    #     # checks whether the instance has already been saved to the database or not.
    #     if not self.id:

    #         latest_season = Season.objects.order_by('-created_at').first()
    #         # we have to set the current_season to false first if not there will be more than 1 true
    #         if latest_season:
    #             latest_season.current_season = False
    #             latest_season.save()
    #         # then set the newly created current_season to be true
    #         self.current_season = True
    #     super(Season, self).save(*args, **kwargs)


# current_date = localtime.now()
# Season.objects.filter(from__lte=current_date, to__gte=current_date
#                       )
