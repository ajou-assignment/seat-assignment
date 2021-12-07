from json import encoder
from django.db.models.query import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.http import response, JsonResponse
from django.http.request import split_domain_port
from django.shortcuts import render
from rest_framework.serializers import Serializer
import numpy as np
import re
from .serializers import mySerializer 
from rest_framework import viewsets      
from .models import *
import backend.algorithm.metaheuristics as mh
import string
import datetime

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return tuple(o)
        elif isinstance(o, UserSet):
            return {"id":o.id, "name":o.name, "satisfaction":o.satisfaction }
        elif isinstance(o, np.integer):
            return int(o)
        elif isinstance(o, np.floating):
            return float(o)
        elif isinstance(o, np.ndarray):
            return o.tolist(o)
        
        return super().default(o)


def postTest(request):
    serializer_class = mySerializer(data=request.POST)
    data = {
        "name" : "Jeong Bo Kyeong",
        "satisfaction" : 26
    }

    # post data form Frontend
    serializer = mySerializer(data=data)
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


def AlgoTest(request):
    data = mh.getSeatData()

    encoder = MyJSONEncoder
    safe = False
    json_dumps_params = {"ensure_ascii": False}
    kwargs = {}

    print("Asdfasfsaf")
    print(data)

    r = JsonResponse(data, encoder, safe, json_dumps_params, **kwargs)
    r.content.decode("utf8")

    # ouput of seats for students by Tabu Search (Shake)
    #return JsonResponse(data, safe=False)
    #return data
    return r

#print(AlgoTest())

'''
    -- 만족도 기준정보 테이블 조회
    Select * from [TB_SATSFACTION_POINT]

    -- 학생 정보 테이블 조회
    Select * from [TB_STUDENT_INFO]

    -- 최근 10회 히스토리 추출
    Select TOP(400) * from [TB_HIST_MATCH] Order by [INSERT_TIME] desc 

    -- 최근 매칭 이력 추가 40번 반복 예정 (1, 2에 실데이터 들어감)
    Insert Into [TB_HIST_MATCH] Values(1, 2, getdate())
'''

def dbSelect(str: string):
    result = ''

    # -- 만족도 기준정보 테이블 조회
    # Select * from [TB_SATSFACTION_POINT]
    if(str == "Select * from [TB_SATSFACTION_POINT]"):
        result = Satisfaction_Point.objects.all()
    # -- 학생 정보 테이블 조회
    # Select * from [TB_STUDENT_INFO]
    elif(str == "Select * from [TB_STUDENT_INFO]"):
        result = Student_Info.objects.all()
    # -- 최근 10회 히스토리 추출
    # Select TOP(400) * from [TB_HIST_MATCH] Order by [INSERT_TIME] desc 
    # https://oneone-note.tistory.com/36
    elif(str == "Select TOP(400) * from [TB_HIST_MATCH] Order by [INSERT_TIME] desc"):
        str2 = re.findall(r'\d', string)
        print(str2)
        num = int(str2[0])
        result = Student_Info.objects.order_by('-insert_time')[:num]
    # -- 최근 매칭 이력 추가 40번 반복 예정 (1, 2에 실데이터 들어감)
    # Insert Into [TB_HIST_MATCH] Values(1, 2, getdate())
    # https://codechacha.com/ko/python-extract-integers-from-string/
    elif(str == "Insert Into [TB_HIST_MATCH] Values(1, 2, getdate())"):
        str2 = re.findall(r'\d', string)
        print(str2)
        num1 = int(str2[0])
        num2 = int(str2[1])
        date = datetime.datetime.now()

        result = {
            "stu_num1"    : num1,
            "stu_num2"    : num2,
            "insert_time" : date,
        }

        # post data form Frontend
        serializer = mySerializer(data=result)
        if serializer.is_valid():
            serializer.save()
        else:
            return "save failed"

    return result