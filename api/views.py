from django.http import response, JsonResponse
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

def test(request):
    data = {
        "name" : "hong seong bin",
        "age" : 26
    }
    return JsonResponse(data)