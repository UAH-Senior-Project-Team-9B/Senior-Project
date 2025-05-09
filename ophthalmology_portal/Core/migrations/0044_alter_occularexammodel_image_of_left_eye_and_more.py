# Generated by Django 5.1.5 on 2025-04-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0043_remove_exammodel_completed_alter_exammodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occularexammodel',
            name='image_of_left_eye',
            field=models.ImageField(upload_to='left_eye/'),
        ),
        migrations.AlterField(
            model_name='occularexammodel',
            name='image_of_right_eye',
            field=models.ImageField(upload_to='right_eye/'),
        ),
    ]
