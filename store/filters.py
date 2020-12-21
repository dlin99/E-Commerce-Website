import django_filters
from .models import Product
from django.forms.widgets import TextInput


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
    	lookup_expr='icontains',
    	widget=TextInput(attrs={'placeholder': 'Search Product'})
    	)

    class Meta:
        model = Product
        fields = ['name']

