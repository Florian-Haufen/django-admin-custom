# Generated by Django 5.0.6 on 2024-05-26 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(null=True)),
                ('is_active', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('patronym', models.CharField(max_length=30, null=True)),
                ('birthday', models.DateField(null=True)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(null=True, upload_to='emp_folder/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', to_field='title')),
            ],
        ),
    ]
