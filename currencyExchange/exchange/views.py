from django.shortcuts import render

# Create your views here.

API_KEY = 'd0764cd0335143af9b924d0e16d9dff2'
BASE_URL = 'https://openexchangerates.org/api/latest.json'


def currency_exchange(request):
    return render(request, 'index.html')