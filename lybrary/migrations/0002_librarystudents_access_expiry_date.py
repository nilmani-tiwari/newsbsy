# Generated by Django 4.1.4 on 2023-01-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lybrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarystudents',
            name='access_expiry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
