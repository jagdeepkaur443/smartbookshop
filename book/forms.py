from django import forms
from .models import Employee_details

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['emp_id', 'emp_name']