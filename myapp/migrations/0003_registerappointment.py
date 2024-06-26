# Generated by Django 5.0.4 on 2024-05-09 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_registerreservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(verbose_name='Data')),
                ('create_at', models.DateField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Registrar Agendamento',
                'verbose_name_plural': 'Registrar Agendamentos',
                'ordering': ['-id'],
            },
        ),
    ]
