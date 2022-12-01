from django.shortcuts import render
from rest_framework import viewsets
from .models import RatingBooks
from .serializers import RatingBooksSerializers

# Create your views here.

class RatingViewSets(viewsets.ModelViewSet):
    queryset = RatingBooks.objects.all()
    serializer_class = RatingBooksSerializers