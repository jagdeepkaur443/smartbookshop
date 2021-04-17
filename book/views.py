from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeForm, AuthorForm, BookForm, CustomerDetailsForm, OrderDetailsForm, WarehouseMainForm, UpdateEmployeeForm
from .models import Employee_details, Book, Author, Customer_Details, Order_details, Warehouse_main
from matplot import views
# Create your views here.

#Views to get data from database
class EmployeeShow(generic.ListView):
    queryset = Employee_details.objects.order_by('emp_id')
    template_name = 'employeeShow.html'

class HomeView(generic.ListView):
    queryset = Book.objects.order_by('book_name')
    template_name = 'index.html'

# Form creation Views
class Employee_details_View(generic.CreateView):
    form_class = EmployeeForm
    model = Employee_details
    template_name = 'addandshow.html'
    success_url = '/'


class AuthorView(generic.CreateView):
    form_class = AuthorForm
    model = Author
    template_name = 'author.html'
    success_url = '/'

class BookView(generic.CreateView):
    form_class = BookForm
    model = Book
    template_name = 'book.html'  
    success_url = '/'

class CustomerDetailsView(generic.CreateView):
    form_class = CustomerDetailsForm
    model = Customer_Details
    template_name = 'customer.html'
    success_url = '/' 

class OrderDetailsView(generic.CreateView):
    form_class = OrderDetailsForm
    model = Order_details
    template_name = 'order.html'
    success_url = '/'

class WarehouseMainView(generic.CreateView):
    form_class = WarehouseMainForm
    model = Warehouse_main
    template_name = 'warehouse.html'
    success_url = '/'


# def post_remove(request, pk):
#     post = get_object_or_404(Book, pk=pk)
#     post.delete()
#     return redirect('/')

class UpdateEmployee(generic.UpdateView):
    form_class = UpdateEmployeeForm
    model = Employee_details
    template_name = 'employeeUpdate.html'
    success_url = '/'