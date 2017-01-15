from django import forms
from ridesharing.models import Ride, RideRequest
NUM_SEATS = (('1', 1),('2',2))

# used by the the above function for the form for posting a new ride
class RideForm(forms.ModelForm):
    class Meta:
        # What model you are trying to create with this form
        model = Ride
        # What fields you want to be able to fill out
        fields = ["first_name", "last_name", "email_address", "phone_number", "destination", "date", "seats_available"]

    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        ),
    )

    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}
        ),
    )

    email_address = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'School Email Address'}
        ),
        # validators=[validators.EmailValidator(message="Your message")]
    )

    phone_number = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Phone Number'}
        ),
    )

    destination = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Destination'}
        ),
    )

    seats_available = forms.ChoiceField(choices = NUM_SEATS,
        label='',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control','id': 'datetimepicker1', 'placeholder':'Date'}
        ),
    )

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequest
        fields = '__all__'
