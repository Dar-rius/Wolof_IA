from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('data', views.data_view, 'data'),
    path('data', views.developer_view, 'developer'),
    path('data', views.ai_view, 'ai')
]