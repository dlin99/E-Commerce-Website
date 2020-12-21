from django import template

register = template.Library() 

from .. filters import ProductFilter
from .. models import Product


@register.inclusion_tag('store/search_bar.html')
def myfilter_search():
	products = Product.objects.all()
	myFilter = ProductFilter(queryset=products)

	return {'myFilterSearchBar': myFilter}


# from .. utils import cartData

# @register.inclusion_tag('store/main.html')
# def cartItems(request):
# 	data = cartData(request)
# 	cartItems = data['cartItems']

# 	return {'cartItems': cartItems}

 