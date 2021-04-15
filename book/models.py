from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name

class Customer_Details(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    customer_contact_no = models.IntegerField()

    def __str__(self):
        return self.customer_name

class Warehouse_main(models.Model):
    warehouse_id = models.IntegerField(unique=True)
    warehouse_location = models.CharField(max_length=200)

    def __str__(self):
        return self.warehouse_location

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    year_Published=models.IntegerField()
    price=models.IntegerField()
    no_of_copies=models.IntegerField()
    author_name=models.ForeignKey(Author, on_delete=models.CASCADE)
    warehouse_location=models.ForeignKey(Warehouse_main, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

class Order_details(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now=True)
    order_quantity = models.CharField(max_length=200)
    customer_name=models.ForeignKey(Customer_Details, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.order_id

class Employee_details(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=200)

    def __str__(self):
        return self.emp_name