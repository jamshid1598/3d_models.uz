from cart.forms import PayForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse, BadHeaderError
from django.core import serializers
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.template import defaultfilters
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from datetime import datetime
from django.db.models import Case, Value, When, Q, F
import json

from product.models import *
from product.forms import ModelSearchForm
from cart.models import *
from core.models import *


from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,    
)
# from .forms import SearchForm
from product.filters import ProductFilter
from download.views import create_verify


class MainView(ListView):
	model=Category
	template_name = "index.html"
	paginate_by = 10


class Categories(View):
	template_name = "kategorya.html"
	context       = {}
	def get(self, request, pk, *args, **kwargs):
		categories  = Category.objects.get(pk=pk)
		models_list = categories.product_category.all()

		paginator     = Paginator(models_list, 24)
		page_num      = paginator.num_pages
		page_indexes  = [x for x in range(1, page_num + 1)]

		print(page_indexes)
	
		page_number 		= request.GET.get('page')
		product_object_list = paginator.get_page(page_number)

		self.context['product_object_list'] = product_object_list
		self.context['page_indexes']		= page_indexes
		self.context["object_list"] 		= models_list
		
		return render(
			request,
			self.template_name,
			self.context
		)


class ModelDetailView(DetailView):
	template_name  = 'Mahsulot.html'
	model          = Product

	slug_field     = 'slug'
	slug_url_kwarg = 'slug'

	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		# images related to 3d model object
		md = Product.objects.get(slug=self.kwargs['slug'])
		context['image_list'] = md.product_images.all()
		
		return context



class PaymentView(LoginRequiredMixin, View):
	template_name = "To'lov.forma.html"
	# context       = {}
	total_price = 0
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			customer = self.request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			print("Order: ", order, '\n', "Created: ", created)
			items = order.orderitem_set.all()
		else:
			items = []
		
		if len(items) > 0:
			for item in items:
				if item.cart_field and item.model.discount:
					self.total_price += item.model.discount
				elif item.cart_field:
					self.total_price += item.model.price

		print(self.total_price)
		payform = PayForm()
		return render(
			request,
			self.template_name,
			{'payform': payform},
		)
	def post(self, request):
		payform = PayForm(request.POST)

		if payform.is_valid():
			number = payform.cleaned_data['number']
			exp_date = payform.cleaned_data['exp_date']
			
			r = create_verify(number, exp_date, self.total_price)
			if 'error' not in r:
					# return redirect('card_verify_code')
				return render(request, "card_verify.html", {
					'token': r['token']
				})
			# else:
		print("Error")
		return redirect('Core:payment-view')


class FreeModelListView(View):
	template_name = "free.html"
	context       = {}

	def get(self, request, *args, **kwargs):
		models_list  = Product.objects.filter(free=True)

		paginator     = Paginator(models_list, 24)
		page_num      = paginator.num_pages
		page_indexes  = [x for x in range(1, page_num + 1)]

		page_number 		= request.GET.get('page')
		product_object_list = paginator.get_page(page_number)

		self.context['product_object_list'] = product_object_list
		self.context['page_indexes']		= page_indexes
		self.context["object_list"] 		= models_list
		
		return render(
			request,
			self.template_name,
			self.context
		)


def download_counter(request):
	slug = request.GET.get('request_data')
	Product.objects.filter(slug = slug).update(downloaded = F('downloaded')+1)
	return HttpResponse(
        json.dumps('Increased'),
        content_type="application/json"
    )


def downloads(request, *args, **kwargs):
	models = Product.objects.all()
	downloads = 0
	if models:
		downloads = sum([product.downloaded for product in models])
		try:
			return JsonResponse({"instance": downloads,}, safe=False, status=200)
		except Exception as e:
			print("Error occured: ", e)
	return Http404

class PortfolioListView(ListView):
	model = PortFolio
	template_name = "portfolio.html"
	paginate_by = 27

class PortfolioDetailView(DetailView):
	model=PortFolio
	template_name = "portfolioKo'rinish.html"
	
	slug_field     = 'slug'
	slug_url_kwarg = 'slug'
	
class VideosListView(ListView):
    model = VideoModel
    template_name = 'Videos.html'
    paginate_by = 15


class DiscuntView(View):
	template_name = "sale.html"
	context={}
	def get(self, request, *args, **kwargs):
		discount_list = []
		
		for product in Product.objects.all():
			if product.discount and product.paid:
				discount_list.append(product)
		
		paginator     = Paginator(discount_list, 24)
		page_num      = paginator.num_pages
		page_indexes  = [x for x in range(1, page_num + 1)]

		page_number 		= request.GET.get('page')
		product_object_list = paginator.get_page(page_number)
		
		self.context['product_object_list'] = product_object_list
		self.context['page_indexes']		= page_indexes
		self.context["object_list"]         = discount_list
		
		return render(
			request,
			self.template_name, 
			self.context
		)



class AboutUsView(View):
	template_name = "about.html"
	context={}
	def get(self, request, *args, **kwargs):
		self.context["object_list"] = AboutUs.objects.all()
		return render(
			request,
			self.template_name, 
			self.context
		)



from users.forms import FeedbackForm

class Contact(View):
	template_name ='Aloqa.html'
	context       = {}

	def get(self, request, *args, **kwargs):
		form                 = FeedbackForm()
		self.context['form'] = form
		
		return render(
			request,
			self.template_name,
			self.context
		)
	
	def post(self, request, *args, **kwargs):
		if request.method == "POST":
			form = FeedbackForm(request.POST)
			if form.is_valid():
				first_name   = form.cleaned_data['first_name']
				last_name    = form.cleaned_data['last_name']
				phone_number = form.cleaned_data['phone_number']
				text         = form.cleaned_data['text']

				try:
					subject    = "Subject"
					thoughts   = f"{first_name} {last_name}dan yangi xabar: \n\n{text}\nTel: {phone_number}"
					sender     = settings.EMAIL_HOST_USER
					recipients = ['dovurovjamshid95@gmail.com']

					send_mail(subject, thoughts, sender, recipients, fail_silently=False)
					  
					messages.success(request, f"{first_name} xabaringiz muvofaqiyatli yuborildi.")
				except BadHeaderError:
					return HttpResponse('Invalid header')
				return redirect('Core:contact-view')
			else:
				for msg in form.errors:
					messages.error(request, f"{msg}")
				return redirect('Core:contact-view')
		self.context = {
			'form': form
		}
		
		return render(
			request, 
			self.template_name,
			self.context
		)

	
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
class LazyEncoder(DjangoJSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return super().default(obj)

def search_query(request, *args, **kwargs):
	query = ''
	images_url = {}

	# data = json.loads(request.body)
	# query = data['query']
	query = request.GET.get('query')
	print(query)

	object_list = None
	if (len(query) > 0) and (query != "" or query != " "):
		print("length: ", len(query))
		object_list = Product.objects.filter(
			Q(name__icontains=query) | Q(slug__icontains=query) | Q(short_info__icontains=query) | Q(description__icontains=query) 
		)
	if object_list.count() > 0:
		for obj in object_list:
			if obj.imageURL:
				images_url[obj.pk] = obj.imageURL
		print(images_url)
		try:
			object_list_json = serializers.serialize('json', object_list, cls=LazyEncoder, ensure_ascii=True)
			# images_url_json =  json.dumps([images_url,])#serializers.serialize('json', [images_url, ])
		except Exception as e:
			print("Error occured: ", e)
		return JsonResponse({"instance":object_list_json, "images_url":images_url}, safe=False, status=200)
	else:
		object_list_json = "nothing"
		return JsonResponse(object_list_json, safe=False, status=200)
	return Http404