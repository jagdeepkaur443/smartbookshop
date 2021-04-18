from django import forms
from .models import Employee_details, Author, Book, Customer_Details, Order_details, Warehouse_main


#CREATION FORMS
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['emp_id', 'emp_name']

        widgets={
            'emp_id': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']
        
        widgets={
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields =['book_name', 'category', 'year_Published', 'price', 'no_of_copies', 'author_name', 'warehouse_location'] 

        widgets={
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'year_Published': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'no_of_copies': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.Select(attrs={'class': 'form-control'}),
            'warehouse_location': forms.Select(attrs={'class': 'form-control'}),

        }

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer_Details
        fields = ['customer_name', 'customer_address', 'customer_contact_no']

        widgets={
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_address': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_contact_no': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order_details
        fields = ['customer_name', 'book_name', 'order_quantity', ]

        widgets={
            'customer_name': forms.Select(attrs={'class': 'form-control'}),
            'book_name': forms.Select(attrs={'class': 'form-control'}),
            'order_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }
                           
class WarehouseMainForm(forms.ModelForm):
    class Meta:
        model = Warehouse_main
        fields = ['warehouse_id', 'warehouse_location']
        
        widgets={
            'warehouse_id': forms.TextInput(attrs={'class': 'form-control'}),
            'warehouse_location': forms.TextInput(attrs={'class': 'form-control'}),
        }


#UPDATE FORMS

class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['emp_id', 'emp_name']

        widgets={
            'emp_id': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order_details
        fields = ['book_name', 'order_quantity']

        widgets={
            'book_name': forms.Select(attrs={'class': 'form-control'}),
            'order_quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateWarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse_main
        fields = ['warehouse_id', 'warehouse_location']

        widgets={
            'warehouse_id': forms.TextInput(attrs={'class': 'form-control'}),
            'warehouse_location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer_Details
        fields = ['customer_name', 'customer_address', 'customer_contact_no']
        
        widgets={
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_address': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_contact_no': forms.TextInput(attrs={'class': 'form-control'}),
        }