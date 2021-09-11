# Generated by Django 2.1.5 on 2021-09-06 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210906_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditpass',
            name='expirationmonth',
            field=models.CharField(choices=[('01 - January', '01 - January'), ('02 - February', '02 - February'), ('03 - March', '03 - March'), ('04 - April', '04 - April'), ('05 - May', '05 - May'), ('06 - June', '06 - June'), ('07 - July', '07 - July'), ('08 - August', '08 - August'), ('09 - September', '09 - September'), ('10 - October', '10 - October'), ('11 - November', '11 - November'), ('12 - December', '12 - December')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='creditpass',
            name='expirationyear',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(3000)]),
        ),
    ]