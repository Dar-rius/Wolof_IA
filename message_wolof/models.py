#Importation des differents modules
from django.db import models

#Choix des sentiments
SENTIMENTS = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative')
)


# creation des modeles 
class Message_wolof(models.Model):
    message = models.TextField()
    emotion = models.CharField(max_length=50, choices=SENTIMENTS, verbose_name='sentiments')


class Sentences_wolof(models.Model):
    sentence = models.TextField()