from django import forms
from .models import Employee_details, Author, Book, Customer_Details, Order_details, Warehouse_main

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['emp_id', 'emp_name']

class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['emp_id', 'emp_name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields =['book_name', 'category', 'year_Published', 'price', 'no_of_copies', 'author_name', 'warehouse_location'] 

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer_Details
        fields = ['customer_name', 'customer_address', 'customer_contact_no']

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order_details
        fields = ['customer_name', 'book_name', 'order_quantity', ]
                           
class WarehouseMainForm(forms.ModelForm):
    class Meta:
        model = Warehouse_main
        fields = ['warehouse_id', 'warehouse_location']