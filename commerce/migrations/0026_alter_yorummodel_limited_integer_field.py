# Generated by Django 4.0.3 on 2022-04-22 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0025_yorummodel_limited_integer_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorummodel',
            name='limited_integer_field',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)]),
        ),
    ]