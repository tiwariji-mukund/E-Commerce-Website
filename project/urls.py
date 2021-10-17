from django.contrib import admin
from django.urls import path,include
from application import views

admin.site.site_header = "Welcome to Pixie Administration"
admin.site.site_title = "Pixie Admin Portal"
admin.site.index_title = "Pixie Developer"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),

]
