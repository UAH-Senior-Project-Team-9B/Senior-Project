# Generated by Django 5.1.5 on 2025-03-31 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_alter_occularexammodel_other_information'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='exammodel',
            unique_together={('date', 'time')},
        ),
    ]
