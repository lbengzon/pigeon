from django import forms
from ridesharing.models import Ride, RideRequest
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
NUM_SEATS = (('1', 1),('2',2))

# used by the the above function for the form for posting a new ride
class RideForm(forms.ModelForm):
    #This field is not in the model. I add this field to the form to add the radio buttons
    #which determines whether colgate is the destination or origin.
    direction = forms.ChoiceField(
        choices=[(x, x) for x in ['Leaving from colgate', 'Going to Colgate']],
        widget=forms.RadioSelect())

    class Meta:
        # What model you are trying to create with this form
        model = Ride
        # What fields you want to be able to fill out
        fields = ["first_name", "last_name", "email_address", "phone_number", "origin", "destination", "date", "seats_available"]

    #when the form is submitted, this will clean the destination field
    def clean_destination(self):
        destination = self.cleaned_data['destination']
        origin = self.data['origin']
        print("desination: " + destination)
        print("origin: " + origin)
        #cant both be empty
        if destination == "" and origin == "":
            raise ValidationError(
                _('Add a destination'),
                code='invalid',
                # params={'value': '42'},
            )
        #if the destination is null
        if destination == "":
            self.cleaned_data['destination'] = "Colgate"
            destination = "Colgate"
        return destination

    def clean_origin(self):
        origin = self.cleaned_data['origin']
        destination = self.data['destination']
        print("desination: " + destination)
        print("origin: " + origin)
        #cant both be empty
        if destination == "" and origin == "":
            raise ValidationError(
                _('Add an origin'),
                code='invalid',
                # params={'value': '42'},
            )
        #if the destination is null
        if origin == "":
            self.cleaned_data['origin'] = "Colgate"
            origin = "Colgate"
        return origin




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

    origin = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Origin'}
        ),
    )

    destination = forms.CharField(
        required=False,
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
            attrs={'class':'form-control','id': 'datetimepicker1','placeholder':'Date' }#,'id': 'datetimepicker1'
        ),
    )


class RideRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RideRequestForm, self).__init__(*args, **kwargs)
        self.fields['ride'].label_from_instance = lambda obj: "%s %s" % (obj.origin, obj.destination)

    class Meta:
        model = RideRequest
        fields = '__all__'
