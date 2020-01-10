from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    # path('', views.homepage, name = "homepage"),
    path('test/', views.index, name = 'test'),
    path('register/', views.register, name = "register"),
    path('', views.register, name = "register"),

]