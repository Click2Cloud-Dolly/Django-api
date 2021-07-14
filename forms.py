from django import forms
from django.forms import fields
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        #db_table = ''
        #managed = True
        #verbose_name = 'ModelName'
        #verbose_name_plural = 'ModelNames'
