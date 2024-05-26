# Generated by Django 5.0.6 on 2024-05-26 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_description_alter_category_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enter', models.DateField(blank=True, null=True)),
                ('date_exit', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.employee')),
            ],
        ),
    ]