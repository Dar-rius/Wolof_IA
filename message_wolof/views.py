from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormMessage
from .models import Message_wolof

# Create your views here.
def index_view(request):

    forms = FormMessage(request.Post)
    
    if forms.is_valid():
        forms.save()
        
    else:
        forms = FormMessage()

    context = {
        'forms': forms
    }
    return render(request, 'message_wolof/index.html', {context})


def data_view(request):
    messages = Message_wolof.objects.all()

    context = {
        "messages": messages
    }

    return render(request, 'message_wolof/data.html', context)


def developer_view(request):
    return render(request, 'message_wolof/developer.html', {})


def ai_view(request):
    return render(request, 'message_wolof/ai.html', {})