from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CheckoutForm
from .models import Order,OrderItem

def home(request):
    products=Product.objects.all()
    return render(request,'store/home.html',{'products':products})
def product_details(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    return render(request,'store/product_detail.html',{'product':product})
def add_to_cart(request,product_id):
    cart= request.session.get('cart',{})
    cart[product_id]=cart.get(product_id,0)+1
    request.session['cart']=cart
    return redirect('cart') 
def cart_view(request):
    cart=request.session.get('cart',{})
    cart_items=[]
    total=0
    for pid,qty in cart.items():
        product=get_object_or_404(Product,id=pid)
        item_total=product.price*qty
        total+=item_total
        cart_items.append({'product':product,'qty':qty,'total':item_total})
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})    

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.isvalid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'store/register.html',{'form':form})
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            for pid, qty in cart.items():
                product = get_object_or_404(Product, id=pid)
                OrderItem.objects.create(order=order, product=product, quantity=qty)
            request.session['cart'] = {}
            return redirect('home')
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {'form': form})

    

