from django.shortcuts import render, Http404

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

#def product_create_view(request):
#	my_form = RawProductForm()
#	if request.method == "POST":
#		my_form = RawProductForm(request.POST)
#		if my_form.is_valid():
#			# now data is good
#			print(my_form.cleaned_data)
#			Product.objects.create(**my_form.cleaned_data)
#		else:
#			print(my_form.errors)
#	context = {
#		"form": my_form
#	}
#	return render(request, "products/product_create.html", context)

def dynamic_lookup_views(request, id):
	try:
		obj = Product.objects.get(id=id)
		context = {
			"spezia": obj
		}
		return render(request, "products/product_detail.html", context)
	except Product.DoesNotExist:
		raise Http404

def render_initial_data(request):
	initial_data ={
		'title' : "My precious spice"
	}
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

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