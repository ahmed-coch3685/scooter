from django.urls import path
from . import views
app_name ="pro"

urlpatterns = [

path('', views.home, name='home'),
    # Products
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

path('categories/', views.categories_list, name='categories_list'),
path('category/<slug:slug>/', views.category_products, name='category_products'),




path('promotions/', views.promotions, name='promotions'),















path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('terms/', views.terms, name='terms'),
path('faq/', views.faq, name='faq'),]
