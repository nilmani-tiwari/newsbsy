from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
# Create your models here.


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    library_name = models.CharField(max_length=200, blank=True, null=True)
    library_code = models.CharField(unique=True, max_length=200, blank=True, null=True)
    library_registration_number=models.CharField( max_length=200, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)
    mobile = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=20,blank=True, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     owner_sign_image = models.ImageField(upload_to='images/', blank=True, null=True)
#     logo_of_school = models.ImageField(upload_to='images/', blank=True, null=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)



class LibraryStudents(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    Full_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth=models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField( max_length=200, blank=True, null=True)
    #mobile= models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mobile= models.CharField(max_length=10, blank=True, null=True)
    blood_group = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=20,blank=True, null=True)
    admission_no = models.CharField(max_length=15, blank=True, null=True)
    Religion = models.CharField(max_length=200, blank=True, null=True)
    reservation_category=models.CharField(max_length=200, blank=True, null=True)
    library_code=models.CharField(max_length=200, null=True,blank=True)
    student_card_number=models.CharField(max_length=200, null=True,blank=True)
    status=models.BooleanField(default=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    #created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)