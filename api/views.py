from django.shortcuts import render
from .models import assigment

from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AssigmentSerializer
from api import serializers


# Create your views here.

@api_view(['GET'])
def taskAll(request):
    tasks = assigment.objects.all()
    serializer = AssigmentSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskNew(request):
    serializer = AssigmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)