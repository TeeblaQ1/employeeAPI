from django.db import models
from django.db.models import Max
# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, null=True, default=None, blank=True, editable=False, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def unique_id(self):
        total_emp = Employee.objects.all().aggregate(id__max=Max('id'))['id__max']
        if total_emp == None:
            return 1
        else:
            return total_emp + 1
    

    def save(self, *args, **kwargs):
        if not self.employee_id:
            value = Employee.unique_id(self)
            self.employee_id = 'E' + '{0:05d}'.format(value)
        return super(Employee, self).save(*args, **kwargs)
