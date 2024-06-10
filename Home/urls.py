from django.urls import path,include
from . import views

urlpatterns = [
path('',views.index, name='index'),
path('about/',views.about, name= 'about'),
path('check/',views.check, name='check'),
path('service/',views.service, name='service'),
path('program/',views.program, name='program'),
path('contact/',views.contact, name='contact'),
# path('register/',views.register, name='register'),
]
