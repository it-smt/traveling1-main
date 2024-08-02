# Generated by Django 5.0.6 on 2024-07-10 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_trip_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='pending_passengers',
            field=models.ManyToManyField(blank=True, related_name='pending_trips', to='main.userprofile'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='trip_passengers', to='main.userprofile'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='main.userprofile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to='main.userprofile')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='main.trip')),
            ],
        ),
    ]