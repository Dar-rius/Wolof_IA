#Importation des differents modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormMessage
from .models import Message_wolof
import sqlite3
import pandas as pd

# Creation des fonctions d'affichage pour les differents routes

#La fonction de d'affichage pour la page principale
def index_view(request):
    # recuperation des donnees des champs du formulaires lorsqu'une methode POST est passe
    form = FormMessage(request.POST)

    #si les donnees sont valides, ils seront enregistre dans la base de donnee
    # et l'utilisateur sera renvoyer vers la page data
    if form.is_valid():
        form.save()

        #Update data in file csv
        connexion_sql = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from message_wolof_message_wolof", connexion_sql)
        df.to_csv("machine_learning/data/messages.csv")

        return redirect('data')
        
    # Si non rien ne sera stocker dans la base de donnees
    else:
        form = FormMessage

    #la page dont retourne la fonction avec les champs du formulaires
    return render(request, 'message_wolof/index.html', {'form': form})

#une fonction qui lorsque le visiteur arrive sur le route "/" il sera renvoyer vers la page home de l'appli (/message_wolof/home/) 
def redirect_view(request):
    #redirection vers la page "home"
    return redirect('home')

#la fonction d'affichage pour la page "data"
def data_view(request):
    #recuperation de toutes les messages en wolof avec leur emotions stocker dans la base de donnees
    messages = Message_wolof.objects.all()

    #la page dont retourne la fonction
    return render(request, 'message_wolof/data.html', {'messages': messages})

#La fonction d'affichage pour la page "ia"
def ai_view(request):

    #la page dont retourne la fonction
    return render(request, 'message_wolof/ai.html', {})