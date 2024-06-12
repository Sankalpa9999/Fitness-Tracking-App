from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('afterlogin/',views.afterlogin, name='afterlogin'),
    path('payment/',views.payment, name='payment'),
    path('high/',views.high, name='high'),
    path('medium/',views.medium, name='medium'),
    path('low/',views.low, name='low'),
    path('trainer/',views.trainer, name='trainer'),
    
    

]
  