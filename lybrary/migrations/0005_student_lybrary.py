# Generated by Django 4.1.4 on 2023-01-26 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lybrary', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lybrary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lybrary.library'),
        ),
    ]
