from django.shortcuts import render

# Create your views here.
from .models import Product

def product_detail_view(request, *args, **kwargs):
	
	obj = Product.objects.get(id=1)

	'''
	context = {
		'title': obj.title,
		'description': obj.description,
		'price': obj.price
	}
	'''
	context = {
		'spezia': obj
	}

	return render(request, "product/detail.html", context)