# Generated by Django 3.2.9 on 2022-05-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_academiccalendar_term_3_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccalendar',
            name='term_3_end_date',
            field=models.DateField(default='2022-1-1'),
        ),
        migrations.AlterField(
            model_name='academiccalendar',
            name='term_3_start_date',
            field=models.DateField(default='2022-1-1'),
        ),
    ]
