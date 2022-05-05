# Generated by Django 4.0.3 on 2022-04-03 16:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0009_remove_kategorimodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorimodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='isim', unique=True),
        ),
    ]