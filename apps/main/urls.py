from django.urls import path
from . views import *
from ..accounts.views import RegisterView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('deals/', DealsView.as_view(), name='deals'),
    path('register/', RegisterView.as_view(), name='register'),

]
