# Generated by Django 5.1 on 2024-09-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallreservationmodel',
            name='guess_count',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
