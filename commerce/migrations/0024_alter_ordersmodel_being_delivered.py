# Generated by Django 4.0.3 on 2022-04-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0023_alter_sepetmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='being_delivered',
            field=models.BooleanField(default=False),
        ),
    ]