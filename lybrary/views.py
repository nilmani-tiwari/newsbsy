from django.shortcuts import render

# Create your views here.
from lybrary.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from lybrary.models import Student
import datetime

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
        
        data = LybraryStudents.objects.filter(lybrary_code=lybrary_code,status=True).values("student_card_number","user_name")
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

#@login_required(login_url='login')
class Index(TemplateView):
    template_name = "lybrary/home.html"
    permission_classes = [IsAuthenticated]
    
   
    def get(self, request):
        
        contex={}
        
        base={ 'base': "lybrary/base.html" }
        contex.update(base)
        print(8888888888888888888888888888888888888888888888888888888888)

        return render(request, self.template_name, contex)


class AddStudents(TemplateView):
    template_name = "lybrary/add_students.html"
    permission_classes = [IsAuthenticated]
    
   
    def post(self, request):
        print(11111111111111111111111111111111111111111)
        full_name=request.POST.get("full_name")
        gender=request.POST.get("gender")
        date_of_birth=request.POST.get("dob")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        Address=request.POST.get("Address")
        access_expiry_date=request.POST.get("access_expiry_date")
        Father_name=request.POST.get("Father_name")
        # full_name=request.POST.get("full_name")
        # full_name=request.POST.get("full_name")
        # full_name=request.POST.get("full_name")
        date_of_birth=datetime.datetime.strptime(date_of_birth, '%d/%m/%Y').strftime('%Y-%m-%d')
        access_expiry_date=datetime.datetime.strptime(access_expiry_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        password="12345"
   
    
        print(request,request.POST,1111111111111111111111111111111111,full_name,date_of_birth)
        
        lybrary=Lybrary.objects.filter(user=request.user.pk).first()
        

        
        # Student(lybrary=lybrary,user_name=user_name,Full_name=Full_name,gender=gender,date_of_birth=date_of_birth,email=email,mobile=mobile,Address=Address,access_expiry_date=access_expiry_date)
        user_name="".join(full_name.split())
        student,created=Student.objects.get_or_create(Full_name=full_name,gender=gender,date_of_birth=date_of_birth,email=email,mobile=mobile,Address=Address,access_expiry_date=access_expiry_date)
        # user, created = User.objects.get_or_create(username=user_name,  is_active=1)
        user_name=user_name+str(student.id)
        student.user_name=user_name
        student.Father_name=Father_name
        student.lybrary=lybrary
        student.password=password
        student.save()  
        
       
     
        user, created = User.objects.get_or_create(username=user_name,  is_active=1)
        user.set_password(password)
        user.groups.add(7) 
        user.save()
        objt, created =LybraryStudents.objects.update_or_create(user=user,user_name=user_name)
        objt.lybrary_code=lybrary.lybrary_code
        print(lybrary.lybrary_code,99999999999999999999999999999999999999999999999)
        objt.password=password
        objt.Full_name = full_name
        objt.Father_name=Father_name
        objt.gender = gender
        objt.date_of_birth = date_of_birth
        objt.email=email
        objt.mobile=mobile
        objt.Address=Address
        objt.access_expiry_date=access_expiry_date
        objt.save()
         
        
        
        
        contex={}
        base={ 'base': "lybrary/base.html" }
        contex.update(base)
        
        

        return render(request, self.template_name, contex)
    
    
class AllStudentsView(TemplateView):
    template_name = "lybrary/all_students_view.html"
    permission_classes = [IsAuthenticated]
    def get(self, request):
        contex={}
        lybrary=Lybrary.objects.filter(user=request.user.pk).first()
        ctc=Student.objects.filter(lybrary=lybrary)
        contex.update({"data":ctc})
        base={ 'base': "lybrary/base.html" }
        contex.update(base)
        return render(request, self.template_name, contex)
    


class EditStudentsView(TemplateView):
    template_name = "lybrary/edit_student_view.html"
    permission_classes = [IsAuthenticated]
    
    def get(self, request,*args,**kwargs):
        idd=kwargs["id"]
        contex={}
        student,created=Student.objects.get_or_create(id=idd)
        contex.update({"std":student})
        base={ 'base': "lybrary/base.html" }
        contex.update(base)
        
        return render(request, self.template_name, contex)
        
    
    def post(self, request,*args,**kwargs):
        idd=kwargs["id"]
        contex={}
        base={ 'base': "lybrary/base.html" }
        contex.update(base)
        
        full_name=request.POST.get("full_name")
        gender=request.POST.get("gender")
        date_of_birth=request.POST.get("date_of_birth")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        Address=request.POST.get("Address")
        access_expiry_date=request.POST.get("access_expiry_date")
        Father_name=request.POST.get("Father_name")
        status=request.POST.get("status")
        status=True if status else False
        # full_name=request.POST.get("full_name")
        # full_name=request.POST.get("full_name")
        # full_name=request.POST.get("full_name")
        print(access_expiry_date,"date_of_birth",date_of_birth,status)
        if "-" in date_of_birth:
            date_of_birth=datetime.datetime.strptime(date_of_birth, '%Y-%m-%d').strftime('%Y-%m-%d')
        else: 
            date_of_birth=datetime.datetime.strptime(date_of_birth, '%d/%m/%Y').strftime('%Y-%m-%d')
            
        if "-" in access_expiry_date:
            access_expiry_date=datetime.datetime.strptime(access_expiry_date, '%Y-%m-%d').strftime('%Y-%m-%d')
        else: 
            access_expiry_date=datetime.datetime.strptime(access_expiry_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        
        password="12345"
        
        lybrary=Lybrary.objects.filter(user=request.user.pk).first()
        
        
        student,created=Student.objects.get_or_create(id=idd)
        
        student.Full_name = full_name
        student.Father_name=Father_name
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.email=email
        student.mobile=mobile
        student.Address=Address
        student.access_expiry_date=access_expiry_date
        student.status=status
        
        student.save()
        
        user, created = User.objects.get_or_create(username=student.user_name,  is_active=1)
        user.set_password(password)
        user.groups.add(7) 
        user.save()
        
        objt, created =LybraryStudents.objects.update_or_create(user=user,user_name=student.user_name)
        objt.lybrary_code=lybrary.lybrary_code
        objt.password=password
        objt.Full_name = full_name
        objt.Father_name=Father_name
        objt.gender = gender
        objt.date_of_birth = date_of_birth
        objt.email=email
        objt.mobile=mobile
        objt.Address=Address
        objt.access_expiry_date=access_expiry_date
        objt.status=status
        objt.save()
        


        return render(request, self.template_name, contex)








