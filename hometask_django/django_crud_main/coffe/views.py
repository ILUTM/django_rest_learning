from .serializers import CoffeeSerializer
from rest_framework import viewsets
from . permissions import CustomPermission
from rest_framework import filters
from .models import Coffee, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated


def show_menu(request):
    coffee_list = Coffee.objects.all()
    comments = Comment.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(
        request,
        'menu/coffe_menu.html',
        {
            'coffee_list': coffee_list,
            'comments': comments,
            'user_authenticated': request.user.is_authenticated
        }
    )


class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def login(request):
    return render(request, 'registration/login.html')


class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
    permission_classes = [CustomPermission, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['drink_type', ]
