# Generated by Django 5.0.6 on 2024-07-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_trip_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]