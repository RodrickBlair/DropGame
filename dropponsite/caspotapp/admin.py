from django.contrib import admin
from .models import Numberplay, TicketSale
# Register your models here.

class TicketSaleAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'num_sell', 'value', 'draw_time', 'draw_date', 'won']

class NumberplayAdmin(admin.ModelAdmin):
    list_display = ['numberplayed', 'mega', 'sale_date', 'draw']


admin.site.register(TicketSale, TicketSaleAdmin)
admin.site.register(Numberplay, NumberplayAdmin)
