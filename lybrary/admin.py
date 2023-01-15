from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Library)
# admin.site.register(LibraryStudents)


@admin.register(LibraryStudents)
class LibraryStudentsAdmin(admin.ModelAdmin):
    list_display = ['user','library_code','user_name', 'student_card_number', 'status','access_expiry_date']
    list_editable = ['user','library_code','user_name', 'student_card_number', 'status','access_expiry_date']

