from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
import json
import datetime 
from .utils import cookieCart, cartData, guestOrder

from django.db.models import F
from django.core.paginator import Paginator

from .filters import ProductFilter
# Create your views here.

def store(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.all()

	paginator = Paginator(products, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {'products': products, 'cartItems': cartItems, 'page_obj': page_obj}

	return render(request, 'store/store.html', context)

def cart(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('ProductId', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)	
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

# add confirmation email functionality
# from django.core.mail import EmailMessage
# from django.conf import settings
# from django.template.loader import render_to_string

from .tasks import send_confirmation_email

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer 
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

	else:
		customer, order = guestOrder(request, data)


	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	# avoid user manipulating total
	# float v.s. decimal.Decimal problem (maybe should change the price in model back to floatField?)
	if float(total) == float(order.get_cart_total):
		order.complete = True
		print(total, order.get_cart_total, 'inside loop')
	
	order.save()

	print(total, order.get_cart_total, type(total), type(order.get_cart_total))
	if order.shipping == True:
		ShippingAddress.objects.create(
			customer=customer,
			order=order, 
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode']
			)

	send_confirmation_email.delay(customer.name, customer.email)

	# template = render_to_string('store/confirmation_email.html', {'name': customer.name})

	# email = EmailMessage(
	# 	'Thanks for purchasing products from our website!',
	# 	template,
	# 	settings.EMAIL_HOST_USER,
	# 	[customer.email],
	# 	)

	# email.fail_silently=False
	# email.send()

	return JsonResponse('Payment submitted...', safe=False)



def item(request, pk):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	product = Product.objects.get(id=pk)
	product.count = F('count') + 1
	product.save()
	product.refresh_from_db()

	context = {'product': product, 'cartItems': cartItems}
	return render(request, 'store/item.html', context)


def search(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.all()
	myFilter = ProductFilter(request.GET, queryset=products)
	results = myFilter.qs 


	context = {
			'cartItems': cartItems,
			'myFilter':myFilter,
			'results': results
			 }
	return render(request, 'store/search.html', context)

