from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request,*args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs0):
	context = {
		"my_text": "This is about us",
		"this_is_true": True,
		"my_html":"<h3>Hello <b>World</b> !</h3>",
		"my_number": 123,
		"my_list": [123, 4242,"Abc",12313]
	}
	return render(request, "about.html", context)