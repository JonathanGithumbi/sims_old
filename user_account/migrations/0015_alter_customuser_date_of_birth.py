# Generated by Django 3.2.9 on 2022-05-06 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0014_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 5, 6, 12, 16, 50, 193827, tzinfo=utc)),
        ),
    ]
