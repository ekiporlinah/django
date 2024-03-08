from django.shortcuts import render
from .forms import RegistrationForm
from .forms import ParticipantForm
from .models import Participant
# Create your views here.
def registration_form(request):
    form = RegistrationForm()
    return render(request, 'registration_form.html',{'form':form})
