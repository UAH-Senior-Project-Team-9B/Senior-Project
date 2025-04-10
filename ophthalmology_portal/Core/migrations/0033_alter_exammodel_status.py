# Generated by Django 5.1.5 on 2025-04-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0032_alter_exammodel_visual_accuity_aided_string_both_distance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='status',
            field=models.CharField(blank=True, choices=[('PENDING', 'Pending'), ('UPCOMING', 'Upcoming'), ('WAITING', 'In Wait Room'), ('PROGRESSING', 'Exam In Progress'), ('COMPLETE', 'Completed')], max_length=16, null=True),
        ),
    ]
