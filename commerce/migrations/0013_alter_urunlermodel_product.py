# Generated by Django 4.0.3 on 2022-04-03 23:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0012_alter_kategorimodel_isim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunlermodel',
            name='product',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
