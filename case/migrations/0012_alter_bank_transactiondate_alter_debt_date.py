# Generated by Django 4.1.3 on 2022-12-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0011_alter_bank_transactiondate_alter_debt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='transactionDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='debt',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]