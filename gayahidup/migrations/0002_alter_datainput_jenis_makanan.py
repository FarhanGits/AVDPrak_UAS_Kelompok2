# Generated by Django 4.2.7 on 2023-11-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gayahidup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datainput',
            name='jenis_makanan',
            field=models.EmailField(choices=[('sehat', 'Sehat'), ('cepatsaji', 'Cepat Saji')], max_length=254),
        ),
    ]
