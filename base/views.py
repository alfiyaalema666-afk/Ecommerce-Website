from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    categories=Category.objects.all()
    trending_products = Product.objects.filter(is_trending=True)

    return render(request, 'home.html', {"categories": categories,"trending_products": trending_products})

def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    return render(request,'category_products.html',{'category': category,'products':products})

def search_product(request):
    query = request.GET.get("q")

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    context = {
        "products": products,
        "query": query,
    }
    return render(request, "search.html", context)

@login_required
def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

@login_required
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        "cart_items": cart_items,
        "total": total
    }

    return render(request, "cart.html", context)

@login_required
def add_to_wishlist(request, id):

    product = Product.objects.get(id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("wishlist")

@login_required
def wishlist(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    )

    context = {
        "wishlist_items": wishlist_items
    }

    return render(request, "wishlist.html", context)

@login_required
def remove_wishlist(request, id):

    item = Wishlist.objects.get(
        id=id,
        user=request.user
    )

    item.delete()

    return redirect("wishlist")

def about(request):
    return render(request,'about.html')

def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})