# Generated by Django 3.2.9 on 2022-05-09 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialaccount',
            name='date_of_payment',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
