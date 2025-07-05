from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home,name='home'),
    path('product/<int:product_id>/',views.product_detail,name='product_detail'),
    path('add-to-cart/<int:product_id>/',views.add_cart_to_cart,name='add_to_cart'),
    path('cart/',views.cart_view,name='cart'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

path('checkout/', views.checkout, name='checkout'),
]
