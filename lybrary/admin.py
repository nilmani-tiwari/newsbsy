from django.contrib import admin
from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.utils import IntegrityError
# Register your models here.
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.models import User


from .models import *

# admin.site.register(LybraryOwner)
# admin.site.register(Lybrary)
# admin.site.register(LybraryStudents)

@admin.register(LybraryOwner)
class LybraryOwnerAdmin(admin.ModelAdmin):
    app_label = 'lybrary'
    list_display = ['user']
    # autocomplete_fields = ['user']

@admin.register(Lybrary)
class LybraryAdmin(admin.ModelAdmin):
    app_label = 'lybrary'
    list_display = ['user']
    # autocomplete_fields = ['user']

@admin.register(LybraryStudents)
class LybraryStudentsAdmin(admin.ModelAdmin):
    app_label = 'lybrary'
    list_display = ['user','lybrary_code','user_name', 'student_card_number', 'status']
    list_editable = ['lybrary_code','user_name', 'student_card_number', 'status']
    search_fields=['lybrary_code','user_name', 'student_card_number', 'status']
    list_filter=['lybrary_code', 'status']
    # autocomplete_fields = ['user']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    app_label = 'lybrary'
    list_display = ["user_name","Full_name","mobile", 'status']
    list_editable = [ 'status']
    search_fields=['user_name',"mobile", 'status']
    # autocomplete_fields = ['lybrary']
    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        try:
            if request.user.is_superuser:
                obj.save(request)
            else:
                lybrary=Lybrary.objects.filter(user=request.user.pk).first()
                obj.lybrary=lybrary

                user_name=obj.user_name
                Full_name=obj.Full_name
                user, created = User.objects.get_or_create(username=user_name,  is_active=1)
                user.set_password("12345")
                user.groups.add(7) 
                user.save()
                objt, created =LybraryStudents.objects.update_or_create(user=user,user_name=user_name)
                objt.lybrary_code=lybrary.lybrary_code
                objt.save()
                
                
                # user=User(username=user_name).save()
                # objt, created LybraryStudents.objects.update_or_create(user=user,user_name=user_name)
                #objt, created = Person.objects.update_or_create(first_name='John', last_name='Lennon')  
                #objt, created LybraryStudents.objects.update_or_create(user=user,user_name=user_name,Full_name=Full_name,gender=gender,email=email,mobile=mobile,status=status,password=password)

                obj.save(request)
        except IntegrityError as e:
            #obj.save(request,commit=False)
            messages.error(request,'Error message')
            obj.delete(request)
            print(e)

    def get_queryset(self, request): 
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(StudentAdmin, self).get_queryset(request) 
        if request.user.is_superuser:
            return qs
        # Lybrary.objects.filter(user=request.user.pk)
        return qs.filter(lybrary__user=request.user.pk)

#     def has_add_permission(self, request):
#         #request.user.groups.filter(name='').exists()
#         return Student.objects.filter(lybrary=3).exists()

    # def has_change_permission(self, request, obj=None):
    #     return request.user.groups.filter(name='Developers').exists()

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.groups.filter(name='Developers').exists()



# from django.contrib import admin


# class FilterUserAdmin(admin.ModelAdmin): 
#     # def save_model(self, request, obj, form, change):
#     #     obj.user = request.user
#     #     obj.save()

#     def get_queryset(self, request): 
#         # For Django < 1.6, override queryset instead of get_queryset
#         qs = super(FilterUserAdmin, self).get_queryset(request) 
#         return qs.filter(created_by=request.user.pk)

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         # the changelist itself
    #         return True
    #     return obj.user == request.user

# class MyModelAdmin(FilterUserAdmin):
#     list_display = ['user_name',"Full_name","mobile", 'status']
#     list_editable = [ 'status']
#     search_fields=['user_name',"mobile", 'status']
    
# admin.site.register(Student, MyModelAdmin)

# class LybraryAdmin(FilterUserAdmin):
#     list_display = ['lybrary_name',"lybrary_code"]
#     list_editable = ['lybrary_name',"lybrary_code"]
#     search_fields=['lybrary_name',"lybrary_code"]
# admin.site.register(Lybrary, LybraryAdmin)
