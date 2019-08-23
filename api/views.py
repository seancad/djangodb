from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import RentalSerializer
from .models import Rental

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all().order_by('price')
    serializer_class = RentalSerializer
