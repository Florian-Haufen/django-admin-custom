# Generated by Django 5.0.6 on 2024-05-26 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_enter', models.TimeField(blank=True, null=True)),
                ('time_exit', models.TimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.employee')),
            ],
        ),
    ]
