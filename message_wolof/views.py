#Importation des differents de  modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormMessage, FormSentences
from .models import Message_wolof
import sqlite3
import pandas as pd
from rest_framework import viewsets, status
from rest_framework.response import Response 
from .serializer import Message_wolof_serializers
import pickle
import sklearn


"""class CustomerView(viewsets.ModelViewSet): 
    queryset = Message_wolof.objects.all() 
    serializer_class = Message_wolof_serializers """

#Une forction permmettant d'utiliser le model afin qu'il fasse des predictions sur les messages
def model_predict(data):
    try:
        model = pickle.load(open("./machine_learning/models/languagesTraitor.sav", 'rb'))
        data = data
        prediction = model.predict(data)
        return int(prediction)

    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 


# Creation des fonctions d'affichage pour les differents routes

#La fonction de d'affichage pour la page principale
def index_view(request):
    # recuperation des donnees des champs du formulaires lorsqu'une methode POST est passe
    error =""
    if request.method == "POST":
        form = FormMessage(request.POST)
        #si les donnees sont valides, ils seront enregistre dans la base de donnee
        # et l'utilisateur sera renvoyer vers la page data
        if form.is_valid():
            Message = form.cleaned_data['message']
            data  = [Message]
            prediction = model_predict(data)
            print(prediction)

            if prediction != 0:
                form.save()
                #Update data in file csv
                connexion_sql = sqlite3.connect("db.sqlite3")
                df = pd.read_sql_query("SELECT * from message_wolof_message_wolof", connexion_sql)
                df.to_csv("machine_learning/data/messages.csv")
                return redirect('data')
            else:
                error = "Veillez entrer une phrase en wolof"

        # Si non rien ne sera stocker dans la base de donnees
    else:
        form = FormMessage

    #la page dont retourne la fonction avec les champs du formulaires
    return render(request, 'message_wolof/index.html', {'form': form, 'error': error})


#une fonction qui lorsque le visiteur arrive sur le route "/" il sera renvoyer vers la page home de l'appli (/message_wolof/home/) 
def redirect_view(request):
    #redirection vers la page "home"
    return redirect('home')


#la fonction d'affichage pour la page "data"
def data_view(request):
    #recuperation de toutes les messages en wolof avec leur emotions stocker dans la base de donnees
    messages = Message_wolof.objects.all()

    #la page dont retourne la fonction
    return render(request, 'message_wolof/messages.html', {'messages': messages})


#La fonction d'affichage pour la page "ia"
def ai_view(request):
    #la page dont retourne la fonction
    return render(request, 'message_wolof/services.html', {})


def testAI_view(request):
    prediction = ""
    if request.method == "POST":
        form = FormSentences(request.POST)

        if form.is_valid():
            form.save()
            #Update data in file csv
            connexion_sql = sqlite3.connect("db.sqlite3")
            df = pd.read_sql_query("SELECT * from message_wolof_sentences_wolof", connexion_sql)
            df.to_csv("machine_learning/data/langues/sentence_test.csv")
            
            Sentence = form.cleaned_data['sentence']
            data  = [Sentence]
            value_predict = model_predict(data)

            if value_predict != 0:
                prediction = "Wolof"
            else: 
                prediction ="Français"
    else:
        form = FormSentences

    #la page dont retourne la fonction avec les champs du formulaires
    return render(request, 'message_wolof/test.html', {'form': form, 'prediction': prediction})