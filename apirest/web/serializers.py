from django.db.models import fields
from django.db.models.base import Model

from rest_framework import serializers
from .models import RatingBooks

class RatingBooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingBooks
        fields = '__all__'