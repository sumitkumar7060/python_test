from django.shortcuts import render
from .serializers import UserSerializer
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . models import *

# Create your views here.


def index(request):
    return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Coursenotes.objects.all()
    serializer_class = UserSerializer
