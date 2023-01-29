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
     
        # usernames = LybraryStudents.objects.all()

        # return Response(usernames)
        data = LybraryStudents.objects.values("student_card_number","user_name")
        result={}
        for i in data:
            key= i['student_card_number']
            value=i['user_name']
            result[key]=value
        return JsonResponse(data=result,safe=False)


    def post(self, request, format=None):
        lybrary_code=request.data.get("lybrary_code")
        date=request.data.get("date")
     
        # usernames = LybraryStudents.objects.all()

        # return Response(usernames)
        #mydata = Member.objects.filter(firstname='Emil').values()
        
        data = LybraryStudents.objects.filter(lybrary_code=lybrary_code).values("student_card_number","user_name")
        result={}
        for i in data:
            key= i['student_card_number']
            value=i['user_name']
            result[key]=value

        # data={"code":request.get("lybrary_code","date":request.get("date"))}
        return JsonResponse(data={"status":True,"result":result},safe=False)






def error_404(request,  *args, **kwargs):
    context={}
  
    return render(request,'error/404.html', context)

def error_500(request,  *args, **kwargs):
    context={}

    return render(request,'error/500.html', context)

# def error_503(request,  *args, **kwargs):
#     context={}
#     data={"test":"503"}
#     context.update(data)
#     urll=request.build_absolute_uri()
#     pth=urll.split("login_user/?next=")
#     url=pth[-1]
#     context.update({"url":url})
#     data=ErrorRecord(error="503",url=url)
#     data.save()
#     return render(request,'500.html', context)


# def error_504(request,  *args, **kwargs):
#     context={}
#     data={"test":"504"}
#     context.update(data)
#     urll=request.build_absolute_uri()
#     pth=urll.split("login_user/?next=")
#     url=pth[-1]
#     context.update({"url":url})
#     data=ErrorRecord(error="504",url=url)
#     data.save()
#     return render(request,'500.html', context)





