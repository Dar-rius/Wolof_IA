from django.db import models
from pkg_resources import require

# Create your models here.
class Message_wolof(models.Model):
    message = models.CharField(max_length=300)
    nom_presonnalite = models.CharField(max_length=100)
    emotion = models.CharField(max_length=50)