from django import forms
from deafculture.models import Participant

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=8)
    password = forms.CharField(max_length=8)
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['firstname', 'lastname', 'phone_number', 'password']
