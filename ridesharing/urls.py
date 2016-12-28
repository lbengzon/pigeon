from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from ridesharing.models import Ride

#the url patterns of the ridesharing app. /ridesharing/...
urlpatterns = [
    #/ridesharing/
    url(r'^$', ListView.as_view(queryset=Ride.objects.all().filter(approved=True).order_by("-date")
                                , template_name = 'ridesharing/rideList.html')),
    url(r'ride/add$', views.ride_create, name='ride-add'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Ride,
                                            template_name = 'ridesharing/ride.html')),
    url(r'ride/request$', views.ride_request, name='ride-request')
]
