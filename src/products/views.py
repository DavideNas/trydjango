from django.shortcuts import render

from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
	if request.method == "POST":
		my_new_title = request.POST.get('title')
		print(my_new_title)
		# Product.objects.create(title=my_new_title)
	
	context = {}
	return render(request, "products/product_create.html", context)

def product_detail_view(request, *args, **kwargs):
	
	obj = Product.objects.get(id=1)

	context = {
		'spezia': obj
	}

	return render(request, "products/product_detail.html", context)