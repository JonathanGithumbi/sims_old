# Generated by Django 3.2.9 on 2022-05-04 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_account', '0004_auto_20220504_2027'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('primary_contact_name', models.CharField(max_length=30)),
                ('primary_contact_phone_number', models.CharField(max_length=14)),
                ('secondary_contact_name', models.CharField(max_length=30)),
                ('seconday_contact_phone_number', models.CharField(max_length=14)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_account.customuser')),
                ('current_grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='current_grade', to='grade.grade')),
                ('grade_admitted_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='grade.grade')),
            ],
        ),
    ]