from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required

def home(request):
    # =========================
    # Categories Slider
    # =========================
    categories = Category.objects.filter(
        available=True
    ).prefetch_related('products')
    # =========================
    # Featured Products Slider
    # =========================
    featured_products = Product.objects.filter(
        available=True,
        is_featured=True
    ).select_related('category')
    # =========================
    # Offers Slider
    # =========================
    offer_products = Product.objects.filter(
       available=True,
        is_offer=True,
        old_price__isnull=False
    ).select_related('category')
    # =========================
    # New Products Slider
    # =========================
    new_products = Product.objects.filter(
       available=True,
        is_new=True
    ).select_related('category')
    # =========================
    # Banner Slider
    # =========================
    banners = Banner.objects.filter(
        available=True
    ).select_related('product')
    
    # حساب عدد عناصر السلة
    cart_items_count = 0
    if request.user.is_authenticated:
        cart = request.user.carts.filter(is_ordered=False).first()
        if cart:
            cart_items_count = cart.items.count()
    else:
        cart_items_count = len(request.session.get('cart', {}))
        
    context = {
        "categories": categories,
        "featured_products": featured_products,
        "offer_products": offer_products,
        "new_products": new_products,
        "banners": banners,
        'cart_items_count': cart_items_count,}
    return render(request, 'home.html', context)



def product_list(request):
    products = Product.objects.filter( available=True)
    featured_products = Product.objects.filter(
        available=True,
        is_featured=True
    ).select_related('category')
    category_slug = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort')
    # فلترة حسب الفئة
    if category_slug:
        products = products.filter(category__slug=category_slug)
    # فلترة حسب السعر
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    # ترتيب
    if sort == "price_asc":
        products = products.order_by("price")
    elif sort == "price_desc":
        products = products.order_by("-price")
    elif sort == "newest":
        products = products.order_by("-created_at")
    categories = Category.objects.filter( available=True)
    context = {"products": products,"featured_products": featured_products,"categories": categories,}
    return render(request, 'scooters/product/product_list.html', context)




def product_detail(request, slug):
    product = get_object_or_404(
        Product,slug=slug,available=True)
    related_products = Product.objects.filter(category=product.category,available=True).exclude(id=product.id)[:4]
    context = {"product": product, "related_products": related_products,}

    return render(request, 'scooters/product/product_detail.html',context)


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'scooters/product/categories.html', {'categories': categories})

def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = category.products.filter(available=True)
    return render(request, 'scooters/product/category_products.html', {
        'category': category,
        'products': products
    })









from django.utils import timezone
def promotions(request):
    now = timezone.now()
    active_promotions = Promotion.objects.filter(active=True, start_date__lte=now, end_date__gte=now)
    return render(request, 'scooters/promotions.html', {
        'promotions': active_promotions
    })













def about(request):
    return render(request, 'scooters/statics/about.html')
def contact(request):
    if request.method == "POST":
        # هنا ممكن تضيف إرسال الايميل أو حفظ الرسالة في DB
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # يمكن حفظها أو إرسال ايميل
        return render(request, 'scooters/statics/contact_succ.html')
    return render(request, 'scooters/statics/contact.html')
def terms(request):
    return render(request, 'scooters/statics/terms.html')
def faq(request):
    faqs = [
        {
            "question": "كيف يمكنني طلب سكوتر؟",
            "answer": "يمكنك إضافة المنتجات إلى السلة ثم إتمام عملية الدفع عند الاستلام."
        },
        {
            "question": "ما مدة شحن الطلب؟",
            "answer": "الطلبات تصل خلال 3-5 أيام عمل حسب المنطقة."
        },
        {
            "question": "هل يوجد ضمان على السكوترات؟",
            "answer": "نعم، جميع المنتجات تأتي مع ضمان سنة كاملة."
        },
        {
            "question": "هل يمكن إرجاع المنتج؟",
            "answer": "يمكنك إرجاع المنتج خلال 7 أيام من تاريخ الشراء بشرط أن يكون في حالته الأصلية."
        },
    ]
    return render(request, 'scooters/statics/faq.html', {'faqs': faqs})
