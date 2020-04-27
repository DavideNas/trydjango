from django.shortcuts import render

from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_detail_view(request, *args, **kwargs):
	
	obj = Product.objects.get(id=1)

	context = {
		'spezia': obj
	}

	return render(request, "products/product_detail.html", context)