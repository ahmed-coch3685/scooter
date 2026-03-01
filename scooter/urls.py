"""
URL configuration for scooter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns =[
    path('admin/', admin.site.urls),

     path('accounts/', include('registrations.urls',namespace="acc")),
     path('', include('scooters.urls',namespace="pro")),
     path('', include('cart.urls',namespace="cart")),
     path('', include('order.urls',namespace="order")),
     path('', include('wishlist.urls',namespace="wl")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)