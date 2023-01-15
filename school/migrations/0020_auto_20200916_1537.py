# Generated by Django 3.0.2 on 2020-09-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_auto_20200907_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_board_school',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ownermaster',
            name='owner_mobile',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='parentsmaster',
            name='Parents_mobile',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='schoolmaster',
            name='mobile',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='staffmaster',
            name='staff_mobile',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='mobile',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]