# Generated by Django 4.0.6 on 2022-08-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspotapp', '0014_alter_numberplay_draw_alter_ticketsale_draw_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplay',
            name='draw',
            field=models.CharField(choices=[('8:30', 'Early Bird'), ('10:30', 'Drive Time'), ('1:00', 'Midday'), ('3:00', 'Afternoon'), ('5:00', 'Evening'), ('8:25', 'Late Night')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticketsale',
            name='draw_time',
            field=models.CharField(choices=[('8:30', 'Early Bird'), ('10:30', 'Drive Time'), ('1:00', 'Midday'), ('3:00', 'Afternoon'), ('5:00', 'Evening'), ('8:25', 'Late Night')], max_length=50),
        ),
    ]
