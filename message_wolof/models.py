from django.db import models

#choice for sentiments
SENTIMENTS = (
    ('Positive', 'Positive'),
    ('Negative', 'Negative')
)

# Create your models here.
class Message_wolof(models.Model):
    message = models.CharField(max_length=300)
    nom_personnalite = models.CharField(max_length=100)
    emotion = models.CharField(max_length=50, choices=SENTIMENTS, verbose_name='sentiments')