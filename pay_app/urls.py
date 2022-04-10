from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('signature', views.signature, name="signature"),
    path('response', views.response, name="response"),
    path('has_eith_file', views.has_eith_file, name="has_eith_file"),
]    
   