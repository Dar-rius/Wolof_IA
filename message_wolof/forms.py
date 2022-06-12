from django.forms import ModelForm
from .models import Message_wolof

class FormMessage(ModelForm):
    class Meta:
        model = Message_wolof
        fields= ['message', 'nom_personnalite', 'emotion']