from django.db import models
from scooters.models import Product

from django.conf import settings
User=settings.AUTH_USER_MODEL



class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_ordered = models.BooleanField(default=False)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    # def total_quantity(self):
    #     return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # variant = models.ForeignKey(ProductVariant, null=True, blank=True, on_delete=models.SET_NULL)
    def total_price(self):
        return self.product.price * self.quantity
    class Meta:
        unique_together = ('cart', 'product')
    def __str__(self):
        return f"{self.quantity} x {self.product.name} = {self.product.price * self.quantity}"


