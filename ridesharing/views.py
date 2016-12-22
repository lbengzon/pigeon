from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from ridesharing.models import Ride
# Create your views here.

def ride_create(request):
    form = RideForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, "ridesharing/ride_form.html", context)

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ["destination", "date"]
