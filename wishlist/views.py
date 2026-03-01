from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required


def get_wishlist(user):
    wishlist, created = Wishlist.objects.get_or_create(user=user)
    return wishlist


@login_required
def wishlist_view(request):
    wishlist = get_wishlist(request.user)
    items = wishlist.items.all()
    return render(request, "scooters/wishlist/wishlist.html", {
        "items": items
    })


@login_required
def add_to_wishlist(request, product_id):

    wishlist = get_wishlist(request.user)

    product = get_object_or_404(Product, id=product_id)

    WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )

    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_wishlist(request, item_id):

    item = get_object_or_404(
        WishlistItem,
        id=item_id,
        wishlist__user=request.user
    )

    item.delete()

    return redirect("wl:wishlist")
