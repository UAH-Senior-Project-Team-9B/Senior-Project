# Generated by Django 5.1.5 on 2025-03-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_alter_prescriptionmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Upcoming', 'upcoming'), ('In Wait Room', 'waiting'), ('In Progress', 'progressing'), ('Completed', 'completed')], max_length=12),
        ),
    ]
