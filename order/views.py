from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.models import Cart


@login_required
def checkout(request):

    cart = Cart.objects.filter(
        user=request.user,
        is_ordered=False
    ).first()

    if not cart:
        return redirect("cart:cart")

    items = cart.items.all()
    total = sum(item.total_price() for item in items)

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        # إنشاء Order
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            total_price=total
        )

        # إنشاء OrderItems
        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )

        # إغلاق السلة
        cart.is_ordered = True
        cart.save()

        return redirect("order:order_success",order.id)

    return render(request, "scooters/order/checkout.html", {
        "items": items,
        "total": total
    })

@login_required
def order_success(request,order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'scooters/order/order_succ.html', {"order": order})

def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'scooters/order/my_orders.html', {'orders': orders})


def order_detail(request, order_id):
    order = Order.objects.filter(id=order_id,user=request.user).first()
    if not order:
        return redirect("order:my_orders")
    return render(request, 'scooters/order/order_detail.html', {'order': order})


