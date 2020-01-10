from django.shortcuts import render
from .models import Shows

# Create your views here.

def home(request):
	return render(request, template_name="pages/home.html", context={"home":Shows.object.all()})

