#Importation des differents modules
from django.forms import ModelForm
from .models import Message_wolof

#creation de formualire
class FormMessage(ModelForm):
    class Meta:
        model = Message_wolof
        fields= ['message', 'emotion']