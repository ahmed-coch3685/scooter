from django.db import models


from django.conf import settings
User=settings.AUTH_USER_MODEL

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
    ]
    STATUS_CHOICES = (
        ("pending", "قيد المراجعة"),
        ("processing", "جارى التجهيز"),
        ("shipped", "تم الشحن"),
        ("delivered", "تم التسليم"),
    )

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    full_name= models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='cod'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is_paid = models.BooleanField(default=False)
    # payment_method = models.CharField(max_length=50, blank=True, null=True)  # مثال: 'Cash', 'Card', 'PayPal'
    # coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)

    # def final_price(self):
    #     total = sum(item.price * item.quantity for item in self.items.all())

    #     if self.coupon:
    #         if self.coupon.discount_type == 'percentage':
    #             total -= total * (self.coupon.discount_value / 100)
    #         else:
    #             total -= self.coupon.discount_value

        # return max(total, 0)
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('scooters.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    def total_price(self):
        return self.price * self.quantity
    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
