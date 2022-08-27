# Generated by Django 4.1 on 2022-08-27 23:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0007_alter_eventos_creador_alter_eventos_participantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='participantes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]