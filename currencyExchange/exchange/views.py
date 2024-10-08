from django.shortcuts import render
import requests

# Create your views here.

API_KEY = 'd0764cd0335143af9b924d0e16d9dff2'
BASE_URL = 'https://openexchangerates.org/api/latest.json'


def currency_exchange(request):
    context = {'error': None}
    if request.method == 'POST':
        try:
            from_currency = request.POST.get('from_currency').upper()
            to_currency = request.POST.get('to_currency').upper()
            amount = float(request.POST.get('amount'))

            if amount <= 0:
                context['error'] = "Amount must be greater than zero."
                return render(request, 'index.html', context)

            response = requests.get(f"{BASE_URL}?app_id={API_KEY}")

            if response.status_code != 200:
                context['error'] = "Failed to retrieve exchange rates. Please try again."
                return render(request, 'index.html', context)

            data = response.json()
            rates = data.get('rates', {})

            if from_currency not in rates or to_currency not in rates:
                context['error'] = "Invalid currency code. Please check and try again."
                return render(request, 'index.html', context)

            from_rate = rates.get(from_currency, 1)
            to_rate = rates.get(to_currency, 1)
            converted_amount = (amount / from_rate) * to_rate

            context.update({
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'converted_amount': converted_amount,
                'error': None
            })

        except ValueError:
            context['error'] = "Please enter a valid amount."
        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"

    return render(request, 'index.html', context)

