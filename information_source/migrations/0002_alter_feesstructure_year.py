# Generated by Django 3.2.9 on 2022-05-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_source', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesstructure',
            name='year',
            field=models.IntegerField(),
        ),
    ]