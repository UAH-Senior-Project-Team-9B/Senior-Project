# Generated by Django 5.1.5 on 2025-03-15 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_alter_exammodel_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exammodel',
            options={'ordering': ['-date', '-time']},
        ),
    ]
