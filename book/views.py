from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeForm, AuthorForm, BookForm, CustomerDetailsForm, OrderDetailsForm, WarehouseMainForm, \
    UpdateEmployeeForm, UpdateOrderForm, UpdateWarehouseForm
from .models import Employee_details, Book, Author, Customer_Details, Order_details, Warehouse_main
from matplot import views
# Create your views here.

#Views to get data from database
class EmployeeShow(generic.ListView):
    queryset = Employee_details.objects.order_by('emp_id')
    template_name = 'show/employeeShow.html'

class OrderShow(generic.ListView):
    queryset = Order_details.objects.order_by('-order_date')
    template_name = 'show/ordershow.html'

class WarehouseShow(generic.ListView):
    queryset = Warehouse_main.objects.all()
    template_name = 'show/warehouseShow.html'

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
    success_url = 'orderShow/'

class WarehouseMainView(generic.CreateView):
    form_class = WarehouseMainForm
    model = Warehouse_main
    template_name = 'warehouse.html'
    success_url = 'warehouseShow/'


# def post_remove(request, pk):
#     post = get_object_or_404(Book, pk=pk)
#     post.delete()
#     return redirect('/')

#update Views

class UpdateEmployee(generic.UpdateView):
    form_class = UpdateEmployeeForm
    model = Employee_details
    template_name = 'update/employeeUpdate.html'
    success_url = '/'

class UpdateOrder(generic.UpdateView):
    form_class = UpdateOrderForm
    model = Order_details
    template_name = 'update/orderUpdate.html'
    success_url = '/'

class UpdateWarehouse(generic.UpdateView):
    form_class = UpdateWarehouseForm
    model = Warehouse_main
    template_name = 'update/warehouseUpdate.html'
    success_url = '/'

#DELETE VIEWS

def data_remove(request, pk):
    employee = get_object_or_404(Employee_details, pk=pk)
    employee.delete()
    return redirect('/')

def order_remove(request, pk):
    order = get_object_or_404(Order_details, pk=pk)
    order.delete()
    return redirect('/')

def about(request):
    return render(request, 'aboutus.html')