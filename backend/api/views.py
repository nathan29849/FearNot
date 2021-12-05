from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calc, TotalData
from .serializers import CalcSerializer, TotalDataSerializer
import random
from datetime import datetime, timedelta


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello API!")

@api_view(['GET'])
def randomAPI(request, id):
    totalCalcs = Calc.objects.all()
    randomCalcs = random.sample(list(totalCalcs), id)   # id는 랜덤으로 나올 개수
    serializer = CalcSerializer(randomCalcs, many=True) # 다양한 내용들에 대해 내부적으로도 직렬화
    return Response(serializer.data)
    

@api_view(['GET'])
def getCoronaAPI(request, start, end):
    start, end = str(start), str(end)
    start_day = datetime(int(start[:4]), int(start[4:6]), int(start[6:]))
    end_day = datetime(int(end[:4]), int(end[4:6]), int(end[6:]))
    total_data = []
    while start_day != end_day:
        total_data.append(TotalData.objects.get(date=start_day))
        start_day += timedelta(days=1) 
    total_data.append(TotalData.objects.get(date=start_day))
    serializer = TotalDataSerializer(total_data, many=True)
    return Response(serializer.data)


    