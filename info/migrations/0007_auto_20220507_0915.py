# Generated by Django 3.2.9 on 2022-05-07 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
        ('info', '0006_auto_20220506_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feesstructure',
            old_name='grade_1_to_3',
            new_name='interview_fee',
        ),
        migrations.RenameField(
            model_name='feesstructure',
            old_name='interview_fee_upper_classes',
            new_name='tuition_fee',
        ),
        migrations.RemoveField(
            model_name='feesstructure',
            name='interview_fee_lower_classes',
        ),
        migrations.RemoveField(
            model_name='feesstructure',
            name='play_group',
        ),
        migrations.RemoveField(
            model_name='feesstructure',
            name='pre_primary1',
        ),
        migrations.RemoveField(
            model_name='feesstructure',
            name='pre_primary2',
        ),
        migrations.RemoveField(
            model_name='feesstructure',
            name='primary_std_4_to_8',
        ),
        migrations.AddField(
            model_name='feesstructure',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grade.grade'),
            preserve_default=False,
        ),
    ]
