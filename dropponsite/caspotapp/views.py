from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from .models import Numberplay, TicketSale
from datetime import datetime, timedelta, date
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm, TicketSaleForm
import pytz
from django.contrib.auth.models import User
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
    weekly_sale = TicketSale.objects.filter(vendor=request.user, draw_date__gte=str(new_date),
                                            draw_date__lte=str(today)).aggregate(Sum('value'))
    today = date.today()
    day_sale = TicketSale.objects.filter(vendor=request.user, draw_date__gte=str(today)).aggregate(Sum('value'))

    winners = TicketSale.objects.filter(vendor=request.user, won=1).aggregate(Sum('value'))

    total_sale = TicketSale.objects.filter(vendor=request.user).aggregate(Sum('value'))

    try:
        p_out = winners['value__sum']
        total_payout = p_out * 30
    except:
        total_payout = 0


    try:
        day_sale = day_sale['value__sum']
        week_sale = weekly_sale['value__sum']
        pay = 10 / 100 * weekly_sale['value__sum']

        total_sale = (total_sale['value__sum'])
        total = total_sale - total_payout
    except:
        total = 0
        day_sale = 0
        week_sale = 0
        pay = 0
    query1 = TicketSale.objects.all().values_list()
    query2 = Numberplay.objects.all().values_list()
    # print(query1[0][5])
    # print(query1[0][4])
    # print(query1)

    dicts = {}

    def findNumber():

        for i in query1:
            uid = i[0]
            j = i[2]
            v = i[3]
            d = i[5]
            t = i[4]
            s = i[6]
            #print(j, d, t)

            for n in query2:
                p = n[1]
                da = n[3]
                ta = n[4]
                #print(p, da, ta)

                if j == p and d == da and t == ta and s == 0:
                    dicts[uid] = uid
                    dicts[uid] = v
                    print(dicts)
                    print('<-----Found Winning number----->')
                    print(j, v, d, t)
                    print('<-----Found Winning number----->')
                    # dick = j, v, t, d
                    # print(dick)
        return dicts


    num = findNumber()
    print(num)
    print('find none')

    context = {
        'total': total,
        'total_payout': total_payout,
        'num': num,
        'weeksale': week_sale,
        'pay': pay,
        'daysale': day_sale,

    }

    return render(request, 'caspotapp/profile.html', context=context)


class WinnersListView(DetailView):
    model = TicketSale
    context_object_name = 'number_detail'
    template_name = 'caspotapp/number_win.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WinnerUpdateView(UpdateView):
    fields = ('won',)
    model = TicketSale

    success_url = '../profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
    today_day = date.today()
    context = {}
    # grabing the lists of input values with getlist()
    # request.POST.get() returns only 1st value but we are working with multiple forms
    num_sells = request.POST.getlist('num_sell')
    values = request.POST.getlist('value')
    #draw_times = request.POST.getlist('draw_time')

    today_time = datetime.now().strftime("%T")
    time = today_time
    print(time)
    hour = int(time[0:2])
    min = int(time[3:5])
    print(hour)
    print(min)
    def draw_t():
        if hour <= int(8) and min < int(25):
            t = '8:30'
            return t
        elif hour < int(10) and min < int(25):
            t = '10:30'
            return t
        elif hour <= int(12) and min < int(25):
            t = '1:00'
            return t
        elif hour <= int(14) and min < int(55):
            t = '3:00'
            return t
        elif hour <= int(16) and min < int(55):
            t = '5:00'
            return t
        elif hour <= int(20) and min < int(20):
            t = '8:20'
            return t
        else:
            t = '8:30'
            return t

    now = str(draw_t())
    print(now)
    # each time this if block is executed if form is submitted with POST method
    if request.method == 'POST':
        print(num_sells)
        print(values)
        #print(draw_times)
        # checking if every field have same number of inputs
        # For Example
        # num_sells = ['value1', 'value2']
        # values = ['value1', 'value2']
        # draw_times = ['value1', 'value2']
        # if any of the input list have less or more number of values, it is not going to save data to database
        if len(num_sells) == len(values):
            # just getting common length of input lists
            total_forms = len(num_sells)
            # from above example, 2 froms are being submitted so each input list have length of 2
            for i in range(total_forms):
                # creating TicketSale objects
                # everytime with field "vendor" having default value of current logged in user (request.user)
                # rest of the fields having values in sequece (as python lists maintain sequence of indexes)
                temp_obj = TicketSale(vendor=request.user, num_sell=num_sells[i], value=values[i],
                                      draw_time=now, draw_date=today_day)
                temp_obj.save()
            total = 0
            for val in values:
                total = total + int(val)
            context['message'] = f'{total_forms} Number(s) sold for ${total}...'

        else:
            # This code block will be executed if there are some missing values or extra values
            context['message'] = "Please check Admin Something went wrong..."

    # everytime we pass "inputs" which essentially are inputs from forms.py file.
    context['inputs'] = TicketSaleForm()

    return render(request, 'caspotapp/make_sale.html', context)


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
