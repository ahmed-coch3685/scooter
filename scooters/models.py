from django.db import models
from django.utils.text import slugify
from unidecode import unidecode
from cloudinary.models import CloudinaryField

from django.conf import settings
User=settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = CloudinaryField('categores')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def products_count(self):
        return self.products.filter(available=True).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
  
class Product(models.Model):
    image =CloudinaryField('products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=3)
    available = models.BooleanField(default=True)
    is_offer = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    slug = models.SlugField(unique=True,blank=True)    
    def save(self,*args,**kwargs):
        if not self.slug:
            base_slug=slugify(unidecode(self.name),allow_unicode=True)
            slug=base_slug
            counte=1
            while Product.objects.filter(slug=slug).exists():
                slug= f"{base_slug}-{counte}"
                counte += 1
            self.slug= slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    



# =========================
# Banner Model
# =========================
class Banner(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='banners')
    image = CloudinaryField('banners')
    discount_percent = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    def __str__(self):
        return f"Banner - {self.product.name}"



class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('products')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.product.name} Image"
    
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.product.name} - {self.key}: {self.value}"


class Promotion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image =CloudinaryField('promotons', blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title











class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=25)
    content = models.TextField( )
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_sessions = models.JSONField(default=list, blank=True)


    def total_likes(self):
        count = len(self.liked_sessions)  # عد اللايكات المباشرة للتعليق
        for reply in self.replies.all():  # لكل رد تابع
            count += reply.total_likes()  # أضف عدد لايكاته recursively
        return count


    def __str__(self):
        return f"{self.user_name} - {self.content[:20]}"


class PostRating(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True, related_name='ratings')
    session_key = models.CharField(max_length=40, null=True, blank=True)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('post', 'session_key')  # كل مستخدم يقيم بوست مرة واحدة فقط
