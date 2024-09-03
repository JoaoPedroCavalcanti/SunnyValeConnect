# Generated by Django 5.1 on 2024-09-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall_reservations', '0003_alter_hallreservationmodel_guess_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hallreservationmodel',
            name='guess_count',
        ),
        migrations.AddField(
            model_name='hallreservationmodel',
            name='guest_count',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
