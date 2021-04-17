"""smartbookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from matplot import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('matplot/', v.home, name='matplot'),
    path('orderGraph', v.order, name='orderGraph'),
    path('bookGraph', v.book, name='bookGraph'),
    path('employeeform/', views.Employee_details_View.as_view(), name='EmployeeDetailForm'),
    path('', views.HomeView.as_view(), name='home'),
    path('authorform/', views.AuthorView.as_view(), name='authorform'),
    path('bookform/', views.BookView.as_view(), name = 'bookform'),
    path('customerDetailsform', views.CustomerDetailsView.as_view(), name ='customerDetailsForm'),
    path('orderDetailsform', views.OrderDetailsView.as_view(), name ='orderDetailsForm'),
    path('warehouseMainform', views.WarehouseMainView.as_view(), name ='WarehouseMainForm'),
    path('employeeShows/', views.EmployeeShow.as_view(), name='employeeShow'),
    path('orderShows/', views.OrderShow.as_view(), name='orderShow'),
    path('warehouseShows/', views.WarehouseShow.as_view(), name='warehouseShow'),
    path('employee_details/edit/<pk>', views.UpdateEmployee.as_view(), name='update_employee'),
    path('order_details/edit/<pk>', views.UpdateOrder.as_view(), name='update_order'),
    path('warehouse_main/edit/<pk>', views.UpdateWarehouse.as_view(), name='update_warehouse'),
    path('employee_details/<pk>/remove/', views.data_remove, name='employee_remove'),
    path('order_details/<pk>/remove/', views.order_remove, name='order_remove'),
]
