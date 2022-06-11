from django.forms import ModelForm
from .models import Message_wolof

class FormMessage(ModelForm):
    model = Message_wolof
    fields= ['message', 'nom_personnalite', 'emotion']