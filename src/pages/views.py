from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request,*args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return HttpResponse("<h1>Hello Django</h1>")

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")