#Importation des differents modules
from django.urls import path
from . import views

#Listes des urls de l'appli avec leur fonction d'affichage
urlpatterns = [
    path('', views.redirect_view, name='redirect'),
    path('accueil/', views.index_view, name='home'),
    path('messages/', views.data_view, name='data'),
    path('services/', views.ai_view, name='ia')
]