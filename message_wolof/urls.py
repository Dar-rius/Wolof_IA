from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('data/', views.data_view, name='data'),
    path('ia/', views.ai_view, name='ia')
]