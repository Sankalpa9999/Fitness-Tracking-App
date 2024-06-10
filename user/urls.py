from django.urls import path,include
from . import views

urlpatterns = [

path('payment/',views.payment, name='payment'),
path('high/',views.high, name='high'),
path('medium/',views.medium, name='medium'),
path('low/',views.low, name='low'),

]