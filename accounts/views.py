from django.shortcuts import render, redirect, reverse

# Create your views here.
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from store.utils import cookieCart, cartData, guestOrder
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required 

@unauthenticated_user
def registerPage(request):
	data = cartData(request)
	cartItems = data['cartItems']
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form': form, 'cartItems': cartItems}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
	data = cartData(request)
	cartItems = data['cartItems']

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('store')
		else:
			messages.info(request, 'username OR password is incorrect')

	context = {'cartItems': cartItems}
	return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def userPage(request):
	data = cartData(request)
	cartItems = data['cartItems']

	customer = request.user.customer

	context = {'customer': customer, 'cartItems': cartItems}
	return render(request, 'accounts/user_profile.html', context)




@login_required(login_url='login')
def userPageUpdate(request):
	data = cartData(request)
	cartItems = data['cartItems']


	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		# form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save() # then re-render to the same page
			return redirect(reverse('user-page'))

	context = {'form': form, 'cartItems': cartItems}
	return render(request, 'accounts/user_profile_update.html', context)


@login_required(login_url='login')
def userOrders(request):
	data = cartData(request)
	cartItems = data['cartItems']


	customer = request.user.customer
	orders = customer.order_set.all().order_by('-date_ordered')

	context = {'cartItems': cartItems, 'orders': orders}
	return render(request, 'accounts/user_orders.html', context)


@login_required(login_url='login')
def userOrdersDetail(request, pk):
	data = cartData(request)
	cartItems = data['cartItems']


	customer = request.user.customer
	order = customer.order_set.get(id=pk)
	print(order)
	orderItems = order.orderitem_set.all()
	print(orderItems)
	context = {'cartItems': cartItems, 'orderItems': orderItems}
	return render(request, 'accounts/user_orders_detail.html', context)