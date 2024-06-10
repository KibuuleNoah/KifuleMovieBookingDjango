from django.shortcuts import render
from store.models import Order


def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "ordersindex.html", context)
