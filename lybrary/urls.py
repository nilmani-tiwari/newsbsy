"""newsbsy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))                  
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
#    path('',views.home, name='home'),
#    path('student/', views.student, name='student'),
#     path('sachin/', views.sachin, name='sachin'),
#     path('parents/', views.parents, name='parents'),
    path('students/', ListUsers.as_view(), name='lybrary_students'),
    path('home/', login_required(Index.as_view()), name='lybrary_home'),
    path('add-student/', login_required(AddStudents.as_view()), name='lybrary_add_students'),
    path('all-students/', login_required(AllStudentsView.as_view()), name='lybrary_all_students'),
    path('edit-student/<id>/', login_required(EditStudentsView.as_view()), name='lybrary_edit_student'),
    path('add/', AddLybrary.as_view(), name='add_lybrary'),
    
]
