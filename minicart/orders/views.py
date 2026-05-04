from django.shortcuts import render,redirect
from . models import order,orderitems
from django.contrib import messages
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=order.objects.get_or_create(
        owner=customer,
        order_status=order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item_from_cart(request,pk):
    item =orderitems.objects.get(pk=pk)
    if item:
       item.delete()
    return redirect('cart')   

def checkout_cart(request):
       if request.POST:
             try:
                 
                 user=request.user
                 customer=user.customer_profile
                 total=float(request.POST.get('total'))

                 order_obj=order.objects.get(
                      owner=customer,
                      order_status=order.CART_STAGE
                 )
                 if order_obj:
                     order_obj.order_status=order.ORDER_COMFIRMED
                     order_obj.total_price=total
                     order_obj.save()
                     status_message="Your Order is Processed. Your Items Will Be Delivered With in 2 Days"
                     messages.success(request,status_message)
                 else:
                     status_message="unable to Processed. no Items Will Be Delivered With in 2 Days"
                     messages.error(request,status_message)
             except Exception as e:
                  status_message="unable to Processed. no Items Will Be Delivered With in 2 Days"
                  messages.error(request,status_message)
             return redirect('cart')

@login_required(login_url='account')  
def show_order(request):
    user=request.user
    customer=user.customer_profile
    all_orders=order.objects.filter(owner=customer)
    context={'orders':all_orders}
    return render(request,'order.html',context)


@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        Product=product.objects.get(pk=product_id)
        ordered_item,created=orderitems.objects.get_or_create(
            product=Product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity=quantity
            ordered_item.save()
        else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
    return redirect('cart')            




