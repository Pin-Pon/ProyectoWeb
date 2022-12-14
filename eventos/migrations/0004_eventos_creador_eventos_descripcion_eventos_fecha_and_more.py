# Generated by Django 4.1 on 2022-08-18 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0003_alter_eventos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mis_eventos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventos',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='eventos',
            name='hora',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='eventos',
            name='lugar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventos',
            name='participantes',
            field=models.ManyToManyField(related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
