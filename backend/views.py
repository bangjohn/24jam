from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.cache import cache
from django.urls import reverse

from backend.models import *
from .forms import *


# Create your views here.
def get_pendingorders():
    pendingorders = transaksitopup.objects.filter(statustransaksiid='2').count()
    return pendingorders

def dashboard(request):
    context = {
        'active_menu_item': 'dashboard',
        'pendingorders': get_pendingorders(),
    }
    return render(request, 'dashboard.html', context)

def orders(request):
    if request.path == '/dashboard/orders/pending':
        # retrieve and display pending orders

        pendingorder = transaksitopup.objects.filter(statustransaksiid='2').order_by('created')
        context = {
            'pendingorders': get_pendingorders(),
            'pendingorder': pendingorder,
            'active_menu_item': 'orders-pending',
            'menu': 'orders',
            'form': formordersupdate,
        }
        # return render(request, 'pending_orders.html', {'orders': orders})
        return render(request, 'orders.html', context)
    if request.path == '/dashboard/orders/new':
        listgame = produkgame.objects.all()
        context = {
            'listgame': listgame,
            'active_menu_item': 'orders-new',
            'menu': 'orders',
            'pendingorders': get_pendingorders(),
            'neworder': '1'
        }
        # retrieve and display pending orders
        # orders = Order.objects.filter(status='pending')
        # return render(request, 'pending_orders.html', {'orders': orders})
        return render(request, 'orders.html', context)
    else:
        # retrieve and display all orders
        # orders = Order.objects.all()
        listorders = transaksitopup.objects.select_related().annotate(nama_game=F('nominaltopupid__produkgameid__title')).order_by('-created')
        context = {
            'active_menu_item': 'orders',
            'menu': 'orders',
            'pendingorders': get_pendingorders(),
            'listorders': listorders
        }
        return render(request, 'orders.html', context)
        # return render(request, 'all_orders.html', {'orders': orders})

def updateorders(request):
    if request.method == "POST":
        getpostdata = request.POST.get('invoice', None)
        data = transaksitopup.objects.filter(invoice=getpostdata)
        for obj in data:
            status = statustransaksi.objects.filter(pk=3).first()
            obj.statustransaksiid = status
            obj.save(update_fields=['statustransaksiid', 'modified'])
        return HttpResponseRedirect(reverse('orders-pending'))
    else:
        return HttpResponse("403 Forbidden", status=403)