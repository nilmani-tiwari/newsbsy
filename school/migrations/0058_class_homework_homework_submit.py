# Generated by Django 3.1.1 on 2021-05-06 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0057_auto_20210327_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_homework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('medium', models.CharField(blank=True, max_length=200, null=True)),
                ('classes', models.CharField(blank=True, max_length=200, null=True)),
                ('section', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='homework_submit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('class_homework_id', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]