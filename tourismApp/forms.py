from django import forms
from .models import TouristDestination

class DestinationForm(forms.ModelForm):
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)

    place_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter place name'})
    )
    weather = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter weather details'})
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'})
    )
    district = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter district'})
    )
    google_map_link = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Google map link'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4})
    )

    class Meta:
        model = TouristDestination
        fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'description', 'image1', 'image2', 'image3']
