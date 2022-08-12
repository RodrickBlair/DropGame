from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Numberplay(models.Model):
    MEGA_BALL = (
        ('Gold', 'Mega'),
        ('White', 'No Mega'),
    )
    DRAW_TIME = (
        ('8:30', 'Early Bird'),
        ('10:30', 'Drive Time'),
        ('1:00', 'Midday'),
        ('3:00', 'Afternoon'),
        ('5:00', 'Evening'),
        ('8:25', 'Late Night'),
    )
    numberplayed = models.PositiveIntegerField()
    mega = models.CharField(max_length=50, choices=MEGA_BALL)
    sale_date = models.DateTimeField('sale date')
    draw = models.CharField(max_length=50, choices=DRAW_TIME)

    def __str__(self):
        return str(self.numberplayed)


class TicketSale(models.Model):
    DRAW_TIMES = (
        ('8:30', 'Early Bird'),
        ('10:30', 'Drive Time'),
        ('1:00', 'Midday'),
        ('3:00', 'Afternoon'),
        ('5:00', 'Evening'),
        ('8:25', 'Late Night'),
    )
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    num_sell = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    draw_time = models.CharField(max_length=50, choices=DRAW_TIMES)
    draw_date = models.DateTimeField(auto_now=True)
    ticket_number = models.PositiveIntegerField(max_length=None, null=True)

    def __str__(self):
        return str(self.num_sell)
