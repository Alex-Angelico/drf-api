from django.shortcuts import render
from rest_framework import generics
from .serializer import JetSerializer
from .models import Jets

# Create your views here.

class JetList(generics.ListAPIView):
  queryset = Jets.objects.all()
  serializer_class = JetSerializer

class JetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Jets.objects.all()
  serializer_class = JetSerializer
