from django.test import TestCase
from django.contrib.auth.models import User

from .models import Employee

class EmployeeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='testpass123')
        testuser1.save()

        testemployee = Employee.objects.create(employee_id=None, first_name='test', last_name='employee', age=45, join_date="2021-05-30")
        testemployee.save()

    def test_entity_content(self):
        employee = Employee.objects.get(id=1)
        first_name = f'{employee.first_name}'
        last_name = f'{employee.last_name}'
        age = f'{employee.age}'
        join_date = f'{employee.join_date}'
        employee_id = 'E' + '{0:05d}'.format(1)
        self.assertEqual(first_name, 'test')
        self.assertEqual(last_name, 'employee')
        self.assertEqual(age, '45')
        self.assertEqual(join_date, "2021-05-30")
        self.assertEqual(employee_id, 'E00001')