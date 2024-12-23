from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('createTourism',TouristDestinationViewSet.as_view(),name='CreateTourism'),
    path('tourist-destinations/', TouristDestinationListView.as_view(), name='tourist-destination-list'),
    path('DestinationView/<int:pk>/',DestinationView.as_view(),name='DestinationDetails'),
    path('DestinationUpdate/<int:pk>/',DestinationUpdate.as_view(),name='DestinationUpdate'),
    path('DestinationDelete/<int:pk>/',DestinationDelete.as_view(),name='DestinationDelete'),


    path('createDestination/',views.create_destination,name='create-Destination'),
    path('DestinationViewAll/',views.DestinationViewAll,name='DestinationView'),
    path('update_destination/<int:id>/',views.update_destination,name='update_destination'),
    path('destination_fetch/<int:id>/',views.destination_fetch,name='destination_fetch'),
    path('destination_delete/<int:id>/',views.destination_delete,name='destination_delete'),
    
    
]