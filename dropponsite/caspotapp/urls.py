from django.urls import path
from . import views
from .views import IndexListView, WinnersListView

app_name = 'caspotapp'

urlpatterns = [
    #path('', IndexListView.as_view(), name='index'),
    path('wins/', WinnersListView.as_view(), name='wins'),
]