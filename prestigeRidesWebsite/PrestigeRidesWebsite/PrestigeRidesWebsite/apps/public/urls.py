
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name="public"
urlpatterns = [
    
    path('', views.index, name="index"),
    path('aboutUs', views.aboutUs, name="aboutUs"),
    path('brands', views.brands, name="brands"),
    path('contactUs', views.contactUs, name="contactUs"),
]