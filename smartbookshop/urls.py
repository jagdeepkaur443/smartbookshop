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
    path('employee_details/edit/<pk>', views.UpdateEmployee.as_view(), name='update_employee'),
    path('admin/', admin.site.urls),
    path('matplot/', v.home, name='matplot'),
    path('employeeform/', views.Employee_details_View.as_view(), name='EmployeeDetailForm'),
    path('', views.HomeView.as_view(), name='home'),
    path('employeeShow/', views.EmployeeShow.as_view(), name='employeeShow'),
    path('authorform/', views.AuthorView.as_view(), name='authorform'),
    path('bookform/', views.BookView.as_view(), name = 'bookform'),
    path('customerDetailsform', views.CustomerDetailsView.as_view(), name ='customerDetailsForm'),
    path('orderDetailsform', views.OrderDetailsView.as_view(), name ='orderDetailsForm'),
    path('warehouseMainform', views.WarehouseMainView.as_view(), name ='WarehouseMainForm'),
]
