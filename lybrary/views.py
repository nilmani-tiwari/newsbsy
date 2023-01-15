from django.shortcuts import render

# Create your views here.
from lybrary.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.http import JsonResponse

class ListUsers(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
     
        # usernames = LibraryStudents.objects.all()

        # return Response(usernames)
        data = LibraryStudents.objects.values("student_card_number","user_name")
        result={}
        for i in data:
            key= i['student_card_number']
            value=i['user_name']
            result[key]=value
        return JsonResponse(data=result,safe=False)


    def post(self, request, format=None):
        lybrary_code=request.data.get("lybrary_code")
        date=request.data.get("date")
     
        # usernames = LibraryStudents.objects.all()

        # return Response(usernames)
        #mydata = Member.objects.filter(firstname='Emil').values()
        
        data = LibraryStudents.objects.filter(library_code=lybrary_code).values("student_card_number","user_name")
        result={}
        for i in data:
            key= i['student_card_number']
            value=i['user_name']
            result[key]=value

        # data={"code":request.get("lybrary_code","date":request.get("date"))}
        return JsonResponse(data=result,safe=False)



