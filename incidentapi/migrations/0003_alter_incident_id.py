# Generated by Django 4.2.2 on 2023-08-05 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('incidentapi', '0002_alter_incident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='id',
            field=models.CharField(default=uuid.UUID('733a52c0-3643-45f3-9e38-c5df9f9f9df0'), max_length=200, primary_key=True, serialize=False),
        ),
    ]