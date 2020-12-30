# E-Commerce-Website 
  - Apps
    - accounts: for customer 
    - sendemail: for contact me page 
    - store: for Product, Order, OrderItem, Shipping Address


# Account 

 - User model and UserCreationForm
```python
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

```

 - ModelForm
```python
from django.forms import ModelForm

# form for changing customer information
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
```

