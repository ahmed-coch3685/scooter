from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *


def cart_details(request):
    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user,is_ordered=False)
        items = cart.items.all() if cart else []
    else:
        items = []
    total = sum(item.total_price() for item in items)
    return render(request, 'scooters/cart/cart_detail.html', {'items': items,'total': total})


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    # الحصول على السلة أو إنشائها
    cart, created = Cart.objects.get_or_create(
        user=request.user,
        is_ordered=False
    )

    # الحصول على CartItem أو إنشائه
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    # لو المنتج موجود بالفعل → زيادة الكمية
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # redirect إلى صفحة السلة
    return redirect("pro:product_detail" , product.slug)

def update_cart_item(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get("quantity"))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect("cart:cart")
