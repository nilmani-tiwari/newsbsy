# Generated by Django 3.0.2 on 2020-09-21 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20200916_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_pack',
            fields=[
                ('massage_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('total_msg', models.CharField(blank=True, max_length=200, null=True)),
                ('sent_msg_to', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='quary_form',
            fields=[
                ('quary_id', models.AutoField(primary_key=True, serialize=False)),
                ('concern_person', models.CharField(blank=True, max_length=200, null=True)),
                ('school_admin_name', models.CharField(blank=True, max_length=200, null=True)),
                ('school_admin_contact', models.CharField(blank=True, max_length=200, null=True)),
                ('school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('school_adress', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('total_students', models.CharField(blank=True, max_length=200, null=True)),
                ('total_teachers', models.CharField(blank=True, max_length=200, null=True)),
                ('number_of_medium', models.CharField(blank=True, max_length=200, null=True)),
                ('class_up_to', models.CharField(blank=True, max_length=200, null=True)),
                ('meeting_conclussion', models.CharField(blank=True, max_length=200, null=True)),
                ('if_next_meeting_date', models.DateField(null=True)),
                ('massage', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(default=datetime.datetime.today, null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
