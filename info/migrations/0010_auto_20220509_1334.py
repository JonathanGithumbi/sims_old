# Generated by Django 3.2.9 on 2022-05-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20220509_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccalendar',
            name='kcpe_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='academiccalendar',
            name='kcpe_start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='academiccalendar',
            name='term_3_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='academiccalendar',
            name='term_3_start_date',
            field=models.DateTimeField(),
        ),
    ]
