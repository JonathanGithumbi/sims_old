# Generated by Django 3.2.9 on 2022-05-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_seconday_contact_phone_number_student_secondary_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hot_lunch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='transport',
            field=models.BooleanField(default=False),
        ),
    ]
