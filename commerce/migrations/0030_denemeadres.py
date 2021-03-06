# Generated by Django 4.0.3 on 2022-05-13 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0029_alter_yorummodel_yorum'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenemeAdres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('ist', 'İstanbul'), ('ist', 'İstanbul')], max_length=50)),
                ('short_description', models.TextField(max_length=150)),
                ('zip', models.CharField(max_length=100)),
                ('adress_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
