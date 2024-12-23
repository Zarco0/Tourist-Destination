from django.contrib import admin

# Register your models here.

from .models import TouristDestination

@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    list_display = ['place_name', 'weather', 'state', 'district']
