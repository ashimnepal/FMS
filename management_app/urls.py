from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.About, name='about'),
    path('enterprise/', views.Enterprise, name='enterprise'),
    path('pricing/', views.Pricing, name='pricing'),
]