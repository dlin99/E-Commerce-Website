from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreateUserForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from store.utils import cookieCart, cartData, guestOrder


def registerPage(request):
	data = cartData(request)
	cartItems = data['cartItems']
	form = CreateUserForm()

	# if request.method == "POST":
	# 	form = CreateUserForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		username = form.cleaned_data.get('username')

	# 		messages.success(request, 'Account was created for ' + username)

	# 		return redirect('login')

	context = {'form': form, 'cartItems': cartItems}
	return render(request, 'accounts/register.html', context)


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
