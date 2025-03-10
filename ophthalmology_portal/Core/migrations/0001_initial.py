# Generated by Django 5.1.5 on 2025-02-17 20:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], max_length=5)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_initial', models.CharField(blank=True, max_length=1)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('social_security_number', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
