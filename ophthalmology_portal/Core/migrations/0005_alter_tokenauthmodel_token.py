# Generated by Django 5.1.5 on 2025-02-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_tokenauthmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenauthmodel',
            name='token',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
