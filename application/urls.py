from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('products.html/', views.products),
    path('about.html/', views.about),
    path('contact.html/', views.contact),
    path('others/', views.others),


]
