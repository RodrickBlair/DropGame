# Generated by Django 4.0.6 on 2022-08-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caspotapp', '0007_alter_numberplay_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberplay',
            name='sale_date',
            field=models.DateField(verbose_name='sale date'),
        ),
    ]
