from django.shortcuts import render
from book.models import Book, Order_details
from .utils import plot, plot2

def  home(request):
    pt = Book.objects.all()
    y= [y.no_of_copies for y in pt]
    x= [x.book_name for x in pt]
    chart= plot(x,y)
    return render (request,'MatplotLib/mat.html',{'chart':chart})

def order(request):
    queryset = Order_details.objects.order_by('-order_quantity')
    y = [x.order_id for x in queryset]
    x = [y.order_quantity for y in queryset]
    chart = plot2(x,y)
    return render (request, 'MatplotLib/order.html', {'chart': chart})

