from django.shortcuts import render
from book.models import Book
from .utils import plot

def  home(request):
    pt = Book.objects.all()
    y= [y.no_of_copies for y in pt]
    x= [x.book_name for x in pt]
    chart= plot(x,y)
    return render (request,'mat.html',{'chart':chart})


# Create your views here.


