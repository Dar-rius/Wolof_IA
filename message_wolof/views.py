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

    return render(request, 'message_wolof/index.html', {'form': form})

def redirect_view(request):
    return redirect('home')


def data_view(request):
    messages = Message_wolof.objects.all()


    return render(request, 'message_wolof/data.html', {'messages': messages})


def ai_view(request):
    return render(request, 'message_wolof/ai.html', {})