# Generated by Django 4.0.4 on 2022-05-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0032_denemeadres_neighborhood_alter_denemeadres_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='denemeadres',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]