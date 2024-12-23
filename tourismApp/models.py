from django.db import models

class TouristDestination(models.Model):
    place_name = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    google_map_link = models.URLField()
    description = models.TextField()
    image1 = models.ImageField(upload_to='destination_images/')
    image2 = models.ImageField(upload_to='destination_images/',blank=True, null=True, help_text="Optional second image")
    image3 = models.ImageField(upload_to='destination_images/',blank=True, null=True, help_text="Optional third image")
