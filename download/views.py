from django.shortcuts import render, get_object_or_404, redirect
from .zip_maker import zip_maker
import requests
from paymeuz.models import Transaction
from cart.models import *


def create_verify(number, exp_date):
    # global price
    # price = amount
    url = "http://127.0.0.1:8000/api/payme/card/create/"
    data = dict(
        id = id,
        params = dict(
            card = dict(
                number = number,
                expire = exp_date,
            ),
            # amount = amount,
            save = True
        )
    )
    response = requests.post(url, json = data)
    result = response.json()

    return result



id = Transaction.objects.all().count() + 1
amount = 0

def card_verify_code(request):
    # global amount
    # amount = 0
    # if request.method == 'GET':
    amount = request.GET.get('amount')
    print(amount)
    if request.method == 'POST':
        url1 = 'http://127.0.0.1:8000/api/payme/card/verify/'
        token = request.POST['token']
        code = request.POST['verify_code']
        # amount = request.POST['amount']
        data1 = dict(
            id = id,
            params = dict(
                token = token,
                code = code
            )
        )
        r = requests.post(url1, json=data1)
        result = r.json()

        url2 = 'http://127.0.0.1:8000/api/payme/payment/'
        data2 = dict(
            id = id,
            params = dict(
                token = token,
                amount = amount,
                account = dict(
                    order_id = id
                )
            )
        )
        rq = requests.post(url2, json=data2)
        rs = rq.json()
        print(rs)
        return redirect('/')
    return render(request, "card_verify.html")





from django.http import HttpResponse
try:
	from StringIO import StringIO
except ImportError:
	from io import StringIO, BytesIO
from zipfile import ZipFile
import os
from django.conf import settings

def make_models_zip(request, *args, **kwargs):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		print("Order: ", order, '\n', "Created: ", created)
		items = order.orderitem_set.all()

	model_locations = []
	for model in  items:
		if model.cart_field:
			model_locations.append(model.model.model_file.path)
	# print("Zip File", zip_maker(model_locations))
	return  zip_maker(model_locations)

