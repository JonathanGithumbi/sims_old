# Generated by Django 3.2.9 on 2022-05-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_account', '0003_financialaccount_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialaccount',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
