from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer


class CarApiView(generics.ListAPIView):

    queryset = Car.objects.all()
    serializer_class = CarSerializer(many=True)
