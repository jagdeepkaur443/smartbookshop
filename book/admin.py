from django.contrib import admin
from .models import Author, Book, Customer_Details, Order_details, Warehouse_main, Employee_details
# Register your models here.
admin.site.register(Author)
admin.site.register(Customer_Details)
admin.site.register(Order_details)
admin.site.register(Warehouse_main)
admin.site.register(Employee_details)
admin.site.register(Book)