from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/',category_products,name='category_products'),
    path("search/", search_product, name="search"),
    path("cart/", cart, name="cart"),
    path("add-to-cart/<int:id>/",add_to_cart,name="add_to_cart"),
    path("wishlist/", wishlist, name="wishlist"),
    path("add-to-wishlist/<int:id>/", add_to_wishlist, name="add_to_wishlist"),
    path("remove-wishlist/<int:id>/", remove_wishlist, name="remove_wishlist"),
    path('about/',about,name='about'),
    path('shop/', shop, name='shop'),
]