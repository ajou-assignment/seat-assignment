from json import encoder
from django.db.models.query import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.http import response, JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
import numpy as np
import backend
from .serializers import TestSerializer 
from rest_framework import viewsets      
from .models import UserSet
import backend.algorithm.metaheuristics as mh

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return tuple(o)
        elif isinstance(o, UserSet):
            return {"id":o.id, "name":o.name, "satisfaction":o.satisfaction }
        
        return super().default(o)


def postTest(request):
    serializer_class = TestSerializer(data=request.POST)
    data = {
        "name" : "Jeong Bo Kyeong",
        "satisfaction" : 26
    }

    # post data form Frontend
    serializer = TestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data)
    else:
        return JsonResponse("save failed")

def GetTest(request):
    # get data from Database
    result = UserSet.objects.all()
    encoder = MyJSONEncoder
    safe = False
    json_dumps_params = {"ensure_ascii": False}
    kwargs = {}

    r = JsonResponse(result, encoder, safe, json_dumps_params, **kwargs)
    r.content.decode("utf8")

    data = [
        {"student1":{'id': 3, 'name': '홍성빈', 'rating': 29.0}, "student2":{'id': 24, 'name': '홍성빈', 'rating': 89.0}}, 
        {"student1":{'id': 5, 'name': '정보경', 'rating': 55.0},  "student2":{'id': 10, 'name': '정보경', 'rating': 88.0}}, 
        {"student1":{'id': 20, 'name': '정명언', 'rating': 94.0},  "student2":{'id': 18, 'name': '정명언', 'rating': 75.0}}, 
        {"student1":{'id': 12, 'name': '박윤우', 'rating': 91.0},  "student2":{'id': 9, 'name': '박윤우', 'rating': 99.0}}, 
        {"student1":{'id': 6, 'name': '서재은', 'rating': 7.0},  "student2":{'id': 1, 'name': '서재은', 'rating': 40.0}}, 
        {"student1":{'id': 8, 'name': '강지혜', 'rating': 93.0},  "student2":{'id': 4, 'name': '강지혜', 'rating': 84.0}}, 
        {"student1":{'id': 16, 'name': '서동찬', 'rating': 95.0},  "student2":{'id': 7, 'name': '서동찬', 'rating': 98.0}}, 
        {"student1":{'id': 2, 'name': '이경민', 'rating': 81.0},  "student2":{'id': 13, 'name': '이경민', 'rating': 88.0}}, 
        {"student1":{'id': 11, 'name': '박수정', 'rating': 44.0},  "student2":{'id': 22, 'name': '박수정', 'rating': 98.0}}, 
        {"student1":{'id': 19, 'name': '이창훈', 'rating': 67.0},  "student2":{'id': 23, 'name': '이창훈', 'rating': 58.0}}, 
        {"student1":{'id': 21, 'name': '박찬우', 'rating': 88.0},  "student2":{'id': 17, 'name': '박찬우', 'rating': 78.0}}, 
        {"student1":{'id': 15, 'name': '서경수', 'rating': 85.0},  "student2":{'id': 14, 'name': '서경수', 'rating': 76.0}}
    ]

    

    return JsonResponse(data, safe=False)


def AlgoTest():
    data = mh.getSeatData()

    # ouput of seats for students by Tabu Search (Shake)
    return JsonResponse(data, safe=False)
    #return data

#print(AlgoTest())