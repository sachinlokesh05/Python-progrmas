from django.shortcuts import render
from testapp.models import Employee
# Create your views here.


def employee_info(request):

    employee = Employee.objects.all()
    return render(request, 'result.html', {'employee': employee})
