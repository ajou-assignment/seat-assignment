from .models import *
import string
import re, datetime
from .serializers import mySerializer 
import numpy as np
from django.db.models.query import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.http import response, JsonResponse
import json

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return tuple(o)
        elif isinstance(o, Hist_Match):
            return {"id":o.id, "stu_num1":o.stu_num1, "stu_num2":o.stu_num2 }
        elif isinstance(o, Satisfaction_Point):
            return {"stu_num_from":o.stu_num_from, "stu_num_to":o.stu_num_to, "point":o.point }
        elif isinstance(o, Student_Info):
            return {"stu_num":o.stu_num, "stu_name":o.stu_name, "stu_gender":o.stu_gender }
        elif isinstance(o, np.integer):
            return int(o)
        elif isinstance(o, np.floating):
            return float(o)
        elif isinstance(o, np.ndarray):
            return o.tolist(o)
        
        return super().default(o)

'''
    -- 만족도 기준정보 테이블 조회
    Select * from [TB_SATSFACTION_POINT]

    -- 학생 정보 테이블 조회
    Select * from [TB_STUDENT_INFO]

    -- 최근 10회 히스토리 추출
    Select TOP(400) * from [TB_HIST_MATCH] Order by [id] desc 

    -- 최근 매칭 이력 추가 40번 반복 예정 (1, 2에 실데이터 들어감)
    Insert Into [TB_HIST_MATCH] Values(1, 2)
'''

def dbSelect(myStr: string):
    # print(myStr)

    # -- 만족도 기준정보 테이블 조회
    # Select * from [TB_SATSFACTION_POINT]
    if("api_satisfaction_point" in myStr):
        r = Satisfaction_Point.objects.all()
    # -- 학생 정보 테이블 조회
    # Select * from [TB_STUDENT_INFO]
    elif("api_student_info" in myStr):
        r = Student_Info.objects.all()
    # -- 최근 10회 히스토리 추출
    # Select TOP(400) * from [TB_HIST_MATCH] Order by [id] desc 
    # https://oneone-note.tistory.com/36
    elif("TOP" in myStr):
        str2 = re.findall(r'\d+', str(myStr))
        # print(str2 + "1")
        num = int(str2[0])
        r = Hist_Match.objects.order_by('-id')[:num]
        # r = Hist_Match.objects.all()
        # print(r)
    # -- 최근 매칭 이력 추가 40번 반복 예정 (1, 2에 실데이터 들어감)
    # Insert Into [TB_HIST_MATCH] Values(1, 2)
    # https://codechacha.com/ko/python-extract-integers-from-string/
    elif("Insert" in myStr):
        # print(myStr.find("Insert"))
        str2 = re.findall(r'\d+', str(myStr))
        # print(str2)
        num1 = int(str2[0])
        num2 = int(str2[1])
        # date = datetime.datetime.now()

        result = {
            "stu_num1"    : num1,
            "stu_num2"    : num2,
        }

        print(result)

        # post data form Frontend
        serializer = mySerializer(data=result)
        if serializer.is_valid():
            serializer.save()
        else:
            return "save failed"
    
    if("Insert" not in myStr):
        encoder = MyJSONEncoder
        serializer = mySerializer(data=encoder)
        safe = False
        json_dumps_params = {"ensure_ascii": False}
        kwargs = {}

        res = JsonResponse(r, encoder, safe, json_dumps_params, **kwargs)
        # res.content.decode("utf8")
        
        result = json.loads(res.content)

    # if("TOP" in myStr):
        # print(result)

    # print(type(result))  
    return result