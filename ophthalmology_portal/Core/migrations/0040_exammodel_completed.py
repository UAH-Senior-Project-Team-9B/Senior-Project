# Generated by Django 5.1.5 on 2025-04-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0039_alter_prescriptionmodel_od_visual_acuity_distance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
