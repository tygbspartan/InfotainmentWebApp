from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
	return render(request=request,template_name="home.html")

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

def user_logout(request):
	logout(request)
	return redirect('main:homepage')

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, f'you have logged as {{ username }}') #.info,.error
				return redirect('main:homepage')

	form = AuthenticationForm()
	return render(request, "main/login.html", 
		context={"form":form})