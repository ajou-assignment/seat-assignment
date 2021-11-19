from django.http import response
from django.shortcuts import render
from .serializers import TodoSerializer 
from rest_framework import viewsets      
from .models import Todo                 
import pyodbc

cnxn = pyodbc.connect

class TodoView(viewsets.ModelViewSet):  
    print(1)
    serializer_class = TodoSerializer   
    queryset = Todo.objects.all() 

def test(requset):
    print(1)
    return response.HttpResponse("asdfasdfsadfsafklnsadfn")