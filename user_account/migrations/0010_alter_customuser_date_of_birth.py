# Generated by Django 3.2.9 on 2022-05-05 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0009_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 16, 9, 33, 198565, tzinfo=utc)),
        ),
    ]
