from rest_framework import serializers
from .models import TouristDestination

class TouristDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristDestination
        fields = ['id', 'place_name', 'weather', 'state', 'district', 'google_map_link', 'description', 'image1','image2','image3']

    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    image3 = serializers.ImageField(required=False)