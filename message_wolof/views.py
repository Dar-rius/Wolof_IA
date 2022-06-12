from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormMessage
from .models import Message_wolof

# Create your views here.
def index_view(request):

    form = FormMessage(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('data')
        
    else:
        form = FormMessage()

    context = {
        'form': form
    }
    return render(request, 'message_wolof/index.html', context)


def data_view(request):
    messages = Message_wolof.objects.all()

    context = {
        "messages": messages
    }

    return render(request, 'message_wolof/data.html', context)


def ai_view(request):
    return render(request, 'message_wolof/ai.html', {})