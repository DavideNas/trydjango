from django.shortcuts import render, Http404, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return render(request, "products/product_list.html", context)

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

def product_delete_view(request, id):
	try:
		obj = get_object_or_404(Product, id=id)
		#POST request
		if request.method == "POST":
			# confirming delete
			obj.delete()
			return redirect('/..')
		context = {
			"spezia": obj
		}
		return render(request, "products/product_delete.html", context)
	except Product.DoesNotExist:
		raise Http404