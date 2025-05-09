# Generated by Django 5.1.5 on 2025-04-13 06:17

import django_cryptography.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0045_alter_exammodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodel',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('upcoming', 'Upcoming'), ('waiting', 'In Wait Room'), ('progressing', 'Exam In Progress'), ('postexam', 'Post Examination'), ('complete', 'Completed')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_both_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_both_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_left_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_left_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_right_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_aided_string_right_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_both_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_both_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_left_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_left_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_right_distance',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='visual_accuity_unaided_string_right_near',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Not Recorded', max_length=255, null=True)),
        ),
    ]
