from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

def order_list(request):
    orders = Order.get_all()
    return render(request, 'order/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/order_form.html', {
        'form': form,
        'title': 'Нове замовлення',
        'back_url': 'order_list'
    })

def order_edit(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/order_form.html', {'form': form, 'action': 'Оновити'})
