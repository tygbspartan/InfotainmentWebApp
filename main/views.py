from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
	return render(request=request,template_name="header.html")

def register(request):
	# return HttpResponse("I am <strong> awesome </strong>")
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('main:homepage')

	form = UserCreationForm()
	return render(request=request, template_name="register.html", 
 	 			context={"form": form}) 
