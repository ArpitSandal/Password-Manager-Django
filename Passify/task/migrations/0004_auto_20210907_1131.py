# Generated by Django 2.1.5 on 2021-09-07 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210906_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditpass',
            name='cardholdername',
        ),
        migrations.AlterField(
            model_name='creditpass',
            name='brand',
            field=models.CharField(choices=[('Rupay', 'Rupay'), ('Visa', 'Visa'), ('Mastercard', 'Mastercard'), ('American Express', 'American Express'), ('Maestro', 'Maestro'), ('UnionPay', 'UnionPay'), ('Other', 'Other')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='creditpass',
            name='expirationyear',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(1999)]),
        ),
    ]