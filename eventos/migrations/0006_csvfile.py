# Generated by Django 4.1 on 2022-08-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_categoria_modalidad_eventos_modalidad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='documents')),
            ],
        ),
    ]
