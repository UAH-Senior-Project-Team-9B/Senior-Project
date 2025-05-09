# Generated by Django 5.1.5 on 2025-03-14 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_exammodel_options_exammodel_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exammodel',
            options={'ordering': ['-date', '-time'], 'permissions': [('patient', 'Patient Permissions'), ('doctor', 'Doctor Permissions'), ('manager', 'Manager Permissions')]},
        ),
        migrations.AlterModelOptions(
            name='occularexammodel',
            options={'permissions': [('patient', 'Patient Permissions'), ('doctor', 'Doctor Permissions'), ('manager', 'Manager Permissions')]},
        ),
        migrations.AlterModelOptions(
            name='prescriptionmodel',
            options={'permissions': [('patient', 'Patient Permissions'), ('doctor', 'Doctor Permissions'), ('manager', 'Manager Permissions')]},
        ),
        migrations.AlterModelOptions(
            name='visualaccuitymodel',
            options={'permissions': [('patient', 'Patient Permissions'), ('doctor', 'Doctor Permissions'), ('manager', 'Manager Permissions')]},
        ),
    ]
