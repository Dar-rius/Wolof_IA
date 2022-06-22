from email import message
from django.test import TestCase
from .models import Message_wolof

# Create your tests here.
class Test_data(TestCase):
    def test_message_wolof(self):
        Message_wolof.objects.create(message="On effectue les testes", emotion="positive")
        Message_wolof.objects.create(message="Les testes ont echouer", emotion="Negative")