# Generated by Django 3.0.2 on 2020-08-22 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('school', '0007_delete_notice_board_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice_board_school',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('Title', models.CharField(blank=True, max_length=64, null=True)),
                ('Details', models.CharField(blank=True, max_length=64, null=True)),
                ('Posted_by', models.CharField(blank=True, max_length=64, null=True)),
                ('Date', models.DateField(null=True)),
            ],
        ),
    ]
