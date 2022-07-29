from dataclasses import field
from rest_framework import serializers
from .models import Message_wolof

class Message_wolof_serializers(serializers.ModelSerializer):
    class Meta:
        model=Message_wolof
        fields = '__all__'