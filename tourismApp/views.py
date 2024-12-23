from django.shortcuts import render,redirect
from rest_framework import generics
from .models import TouristDestination
from .serializers import TouristDestinationSerializer
from .forms import *
import requests
from django.contrib import messages

class TouristDestinationViewSet(generics.ListCreateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class TouristDestinationListView(generics.ListAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class DestinationView(generics.RetrieveAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

class DestinationUpdate(generics.RetrieveUpdateAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

    def update(self, request, *args, **kwargs):
        print("Request Data:", request.data)
        print("Uploaded Files:", request.FILES)
        return super().update(request, *args, **kwargs)


class DestinationDelete(generics.DestroyAPIView):
    queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer

# Connecting to frontend

def create_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Save the destination instance
                destination = form.save()

                # API endpoint URL
                api_url = 'http://127.0.0.1:8000/createTourism'

                # Prepare data and files for the API request
                data = {
                    'place_name': destination.place_name,
                    'weather': destination.weather,
                    'state': destination.state,
                    'district': destination.district,
                    'google_map_link': destination.google_map_link,
                    'description': destination.description,
                }

                # Handle the image fields
                files = {}
                if destination.image1:
                    files['image1'] = destination.image1
                if destination.image2:
                    files['image2'] = destination.image2
                if destination.image3:
                    files['image3'] = destination.image3
                response = requests.post(api_url, data=data, files=files)
                

                if response.status_code == 201:
                    messages.success(request, 'Destination created successfully and synced with the API.')
                else:
                    messages.error(request, f'Failed to sync with API. Status: {response.status_code}, Message: {response.text}')
            except requests.RequestException as e:
                messages.error(request, f'Error during API request: {str(e)}')
            return redirect('create-Destination')  # Redirect to a destination list view
        else:
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        form = DestinationForm()

    return render(request, 'create-destination.html', {'form': form})

def DestinationViewAll(request):
    data=TouristDestination.objects.all()

    api_url = 'http://127.0.0.1:8000/tourist-destinations/'

    return render(request,'DestinationView.html',{'data':data})



def update_destination(request, id):
    api_url = f'http://127.0.0.1:8000/DestinationUpdate/{id}/'

    # Handle GET request: Fetch and display existing data
    if request.method == 'GET':
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'destination_update.html', {'destination': data})
        else:
            messages.error(request, 'Failed to fetch destination details.')
            return redirect('DestinationView')

    # Handle POST request: Submit updated data
    elif request.method == 'POST':
        placename = request.POST['place_name']
        weather = request.POST['weather']
        state = request.POST['state']
        district = request.POST['district']
        google_map_link = request.POST['google_map_link']
        description = request.POST['description']

        # Handle file uploads
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')

        data = {
            "place_name": placename,
            "weather": weather,
            "state": state,
            "district": district,
            "google_map_link": google_map_link,
            "description": description
        }

        # Prepare files dictionary
        files = {}
        if image1:
            files['image1'] = image1
        if image2:
            files['image2'] = image2
        if image3:
            files['image3'] = image3

        response = requests.put(api_url, data=data, files=files)

        if response.status_code == 200:
            messages.success(request, 'Destination Updated Successfully')
            return redirect('DestinationView')
        else:
            messages.error(request, f'Error Submitting data to the REST API: {response.status_code} - {response.text}')

    # In case of any unexpected method, redirect
    return redirect('DestinationView')




def destination_fetch(request, id):
    api_url = f'http://127.0.0.1:8000/DestinationView/{id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        tourism = data['Description'].split('.') if 'Description' in data else []
        return render(request, 'Desti_fetch.html', {'destination': data, 'tourism': tourism})
    return render(request, 'Desti_fetch.html')

def destination_delete(request, id):
    api_url = f'http://127.0.0.1:8000/DestinationDelete/{id}/'
    response = requests.delete(api_url)

    if response.status_code == 204:  # Success response code for deletion
        messages.success(request, 'Destination deleted successfully.')
    else:
        messages.error(request, f'Failed to delete item. Status code: {response.status_code}')
    return redirect('DestinationView')
