from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from ridesharing.models import Ride, RideRequest
from django.views.generic import ListView
from django.shortcuts import redirect


# Create your views here.

#the view for the the list of approved rides
def list_rides(request):
    #The return the list view of ride objects that have been approved sorted by the earliest date
    return ListView.as_view(queryset=Ride.objects.filter(approved=True).order_by("-date"),
                                template_name='ridesharing/rideList.html')(request)


# returns the view for the ride form
def ride_create(request):
    # create the form you want to add to the html page
    form = RideForm(request.POST or None)

    # make sure form is valid
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    # create a context to pass into the html page
    context = {
        "form": form,
    }
    # return the ride_form.html page passing in the context of the form
    return render(request, "ridesharing/ride_form.html", context)


# this returns the view for requesting a ride
# it is called when you submit the ride-request form
# or when you are redirected to the page by clicking on a button from another page like the ride-list page
def ride_request(request):
    # if you were redirected from the ride list page
    if (request.method == 'GET'):
        # get the ride id from the get request (its a url parameter)
        ride_id = request.GET.get("request-ride-btn")
        initial_ride = None
        # get the query set to of all the approved rides
        queryset = Ride.objects.filter(approved=True).order_by("-date")
        # get the ride object that corresponds to the id if there was a ride id
        if (ride_id != None):
            initial_ride = next(iter(queryset.filter(id=ride_id) or []), None)
        # create the form and set the inital value to the ride corresponding the ride id
        form = RideRequestForm(initial={'ride': initial_ride})
        # Set the query set
        form.fields['ride'] = forms.ModelChoiceField(queryset=queryset)
    # this is what is run after you submit the form
    else:
        form = RideRequestForm(request.POST or None)
        # make sure form is valid
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # if we want to redirect we should redirect over here

    # create a context to pass into the html page
    context = {
        "form": form,
    }
    # return the ride_form.html page passing in the context of the form so the html can display the form
    return render(request, "ridesharing/ride_form.html", context)




# used by the the above function for the form for posting a new ride
class RideForm(forms.ModelForm):
    class Meta:
        # What model you are trying to create with this form
        model = Ride
        # What fields you want to be able to fill out
        fields = ["name", "email_address", "phone_number", "destination", "date", "time", "seats_available"]


class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = '__all__'
