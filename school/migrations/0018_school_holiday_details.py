# Generated by Django 3.0.2 on 2020-08-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_school_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_holiday',
            name='details',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]