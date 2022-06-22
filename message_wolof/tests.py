#importer les modules
from django.test import TestCase
from .models import Message_wolof

#Creation des cas de testes 
class Test_data(TestCase):
    #Une fonction permettant de faire des testes sur les modeles
    def test_message_wolof(self):
        messages = Message_wolof()
        messages.message = "On effectue les testes"
        messages.emotion = "Positive"

        self.assertEqual( messages.message, "On effectue les testes")
        self.assertEqual( messages.emotion, "Positive")