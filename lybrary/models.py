from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
# Create your models here.



class LybraryOwner(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    owner_gender = models.CharField(max_length=10, blank=True, null=True)
    #owner_date_of_birth=models.DateField(blank=True,null=True)
    owner_date_of_birth=models.CharField(max_length=10, blank=True, null=True)
    owner_email = models.CharField( max_length=200, blank=True, null=True)
    owner_mobile = models.CharField(max_length=10,  blank=True, null=True)
    owner_image = models.ImageField(upload_to='images/', blank=True, null=True)
    owner_qualification = models.CharField(max_length=200, blank=True, null=True)
    owner_address = models.CharField(max_length=200, blank=True, null=True)
    owner_city = models.CharField(max_length=200, blank=True, null=True)
    owner_pincode = models.CharField(max_length=20,blank=True, null=True)
    lybrary_code=models.CharField(max_length=200, null=True,blank=True)
    created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.owner_name


class Lybrary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    lybrary_id = models.AutoField(primary_key=True)
    lybrary_name = models.CharField(max_length=200, blank=True, null=True)
    lybrary_code = models.CharField(unique=True, max_length=200, blank=True, null=True)
    lybrary_registration_number=models.CharField( max_length=200, blank=True, null=True)
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

    def __str__(self):
        return str(self.lybrary_id)+" "+str(self.lybrary_name)


class LybraryStudents(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    Full_name = models.CharField(max_length=200, blank=True, null=True)
    Father_name = models.CharField(max_length=200, blank=True, null=True)
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
    lybrary_code=models.CharField(max_length=200, null=True,blank=True)
    student_card_number=models.CharField(max_length=200, null=True,blank=True)
    status=models.BooleanField(default=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    access_expiry_date=models.DateTimeField(blank=True, null=True)
    #created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.user_name = self.user.username
        super(LybraryStudents, self).save(*args, **kwargs)


class Student(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    lybrary = models.ForeignKey('Lybrary', on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    Full_name = models.CharField(max_length=200, blank=True, null=True)
    Father_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth=models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField( max_length=200, blank=True, null=True)
    #mobile= models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    mobile= models.CharField(max_length=10, blank=True, null=True)
    # blood_group = models.CharField(max_length=200, blank=True, null=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    # city = models.CharField(max_length=200, blank=True, null=True)
    # pincode = models.CharField(max_length=20,blank=True, null=True)
    # admission_no = models.CharField(max_length=15, blank=True, null=True)
    # Religion = models.CharField(max_length=200, blank=True, null=True)
    # reservation_category=models.CharField(max_length=200, blank=True, null=True)
    # lybrary_code=models.CharField(max_length=200, null=True,blank=True)
    # student_card_number=models.CharField(max_length=200, null=True,blank=True)
    status=models.BooleanField(default=True)
    password=models.CharField(max_length=200, blank=True, null=True)
    access_expiry_date=models.CharField(max_length=10,blank=True, null=True)
    #created_on = models.DateTimeField(default=datetime.now, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        
        # self.user_name = self.user.pk
        
        super(Student, self).save(*args, **kwargs)

    class Meta:
       unique_together = ("lybrary", "user_name")