# Generated by Django 4.0.6 on 2022-08-13 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caspotapp', '0004_alter_ticketsale_ticket_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketsale',
            name='ticket_number',
        ),
    ]