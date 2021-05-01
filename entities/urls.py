from django.urls import path
from .views import EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('<employee_id>/', EmployeeDetailView.as_view()),
    path('', EmployeeListView.as_view()),
]
