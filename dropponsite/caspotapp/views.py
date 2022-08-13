from django.shortcuts import render
from django.views.generic import ListView
from .models import Numberplay, TicketSale
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, TicketSaleForm
import pytz
from django.forms.models import modelformset_factory
from django.db.models import Sum


# Create your views here.
class IndexListView(ListView):
    model = Numberplay
    template_name = 'caspotapp/index.html'

    def get_context_data(self, **kwargs):
        today = datetime.today()
        days_back = timedelta(-7)
        under_date = today + days_back
        today = today.strftime("%Y-%m-%d")
        under_date = under_date.strftime("%Y-%m-%d")
        number_play = Numberplay.objects.filter(sale_date__startswith=today)
        kent_numbers = Numberplay.objects.filter(sale_date__startswith=under_date)
        context = {
            "today_date": today,
            "under_date": under_date,
            "number_play": number_play,
            "kent_numbers": kent_numbers,
        }
        return context


@login_required
def profile(request):
    today_number = date.today().weekday()

    def number():
        if today_number == 0:
            days_back = date.today() + timedelta(-1)
            return days_back
        elif today_number == 1:
            days_back = date.today() + timedelta(-2)
            return days_back
        elif today_number == 2:
            days_back = date.today() + timedelta(-3)
            return days_back
        elif today_number == 3:
            days_back = date.today() + timedelta(-4)
            return days_back
        elif today_number == 4:
            days_back = date.today() + timedelta(-5)
            return days_back
        elif today_number == 5:
            days_back = date.today() + timedelta(-6)
            return days_back
        elif today_number == 6:
            days_back = date.today() + timedelta(-7)
            return days_back
        else:
            return 0

    new_date = number()
    today = date.today() + timedelta(1)
    weekly_sale = TicketSale.objects.filter(draw_date__gte=str(new_date),
                                            draw_date__lte=str(today)).aggregate(Sum('value'))
    today = date.today()
    day_sale = TicketSale.objects.filter(draw_date__gte=str(today)).aggregate(Sum('value'))
    print(day_sale)


    try:
        day_sale = day_sale['value__sum']
        week_sale = weekly_sale['value__sum']
        pay = 10 / 100 * weekly_sale['value__sum']
    except:
        day_sale = 0
        week_sale = 0
        pay = 0


    context = {
        'weeksale': week_sale,
        'pay': pay,
        'daysale': day_sale
    }

    return render(request, 'caspotapp/profile.html', context=context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))

            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'caspotapp/login.html', {})


def make_sale(request):
    # form = TicketSaleForm(request.POST or None)
    #TicketSaleFormset = modelformset_factory(TicketSale, form=TicketSaleForm, extra=0)
    #formset = TicketSaleFormset(request.POST or None, )
    if request.method == "POST":

        numbers = request.POST['number']
        values = request.POST["value"]
        number2 = request.POST or None["number2"]
        value2 = request.POST or None["value2"]
        print(numbers)
        print(values)
        print(number2)
        print(value2)
        #print(values)
    #if formset.is_valid():
     #   formset.save()
    #    context['formset'] = TicketSaleFormset()
    return render(request, 'caspotapp/make_sale.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        # CHECK IF FORM VALID

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'caspotapp/registration.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))

            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'caspotapp/login.html', {})
