# Generated by Django 3.1.1 on 2021-03-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0054_attendance_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='parents_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=64, null=True)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
