from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from ridesharing.models import Ride


# Create your views here.

#this function is called when you access the /ridesharing/ride/add
def ride_create(request):
    #create the form you want to add to the html page
    form = RideForm(request.POST or None)
    #make sure form is valid
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    #create a context to pass into the html page
    context = {
        "form": form,
    }
    #return the ride_form.html page passing in the context of the form
    return render(request, "ridesharing/ride_form.html", context)


# used by the the above function for the form for posting a new ride
class RideForm(forms.ModelForm):
    class Meta:
        # What model you are trying to create with this form
        model = Ride
        # What fields you want to be able to fill out
        fields = ["destination", "date"]
