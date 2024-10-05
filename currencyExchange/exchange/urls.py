from django.urls import path
from . import views

urlpatterns = [
    path('', views.currency_exchange, name='currency_exchange')
]