# Generated by Django 3.1.1 on 2021-03-27 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0056_parents_msg_sender_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_pack',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
