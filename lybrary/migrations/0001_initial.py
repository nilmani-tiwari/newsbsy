# Generated by Django 4.1.4 on 2022-12-16 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('library_id', models.AutoField(primary_key=True, serialize=False)),
                ('library_name', models.CharField(blank=True, max_length=200, null=True)),
                ('library_code', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('library_registration_number', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('mobile', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryStudents',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_name', models.CharField(blank=True, max_length=200, null=True)),
                ('Full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('admission_no', models.CharField(blank=True, max_length=15, null=True)),
                ('Religion', models.CharField(blank=True, max_length=200, null=True)),
                ('reservation_category', models.CharField(blank=True, max_length=200, null=True)),
                ('library_code', models.CharField(blank=True, max_length=200, null=True)),
                ('student_card_number', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
