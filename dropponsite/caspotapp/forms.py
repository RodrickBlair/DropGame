from django import forms
from django.contrib.auth.models import User
from .models import TicketSale


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class TicketSaleForm(forms.ModelForm):
    class Meta:
        model = TicketSale
        fields = ['vendor', 'num_sell', 'value',
                  'draw_time', 'draw_time', 'ticket_number']
