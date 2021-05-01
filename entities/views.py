from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Employee
from .serializers import EmployeeSerializer
from django.views.generic.base import TemplateResponseMixin
# Create your views here.
class EmployeeListView(generics.ListCreateAPIView):
    '''
    This generates a list view of all employee entities
    '''
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    This generates a detailed view of specified employee entity using the unique employee ID generated.
    Employee ID usually starts with 'E' and has 5 digits generated sequentially. E.g. 'E00005'
    '''
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id'

