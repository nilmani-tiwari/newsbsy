# Generated by Django 3.0.2 on 2020-08-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20200824_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_library',
            fields=[
                ('school_library_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('Book_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Writter_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Class', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]