from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import EmployeeForm
from .models import Employee_details, Book


# Create your views here.
class HomeView(generic.ListView):
    queryset = Book.objects.order_by('-created_on')
    template_name = 'updatebook.html'

class Employee_details_View(generic.CreateView):
    form_class = EmployeeForm
    model = Employee_details
    template_name = 'addandshow.html'
    success_url = '/'