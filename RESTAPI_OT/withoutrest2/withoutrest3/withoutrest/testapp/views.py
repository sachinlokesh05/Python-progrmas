# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
# Create your views here.
import json
from django.http import HttpResponse
class EmployeeDetaiils(View):
    def get(self,request):
        #getting employee data of first
        emp = Employee.objects.get(id=3)
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }
        #employee data converting into <dict>
        data = json.dumps(emp_data)
        return HttpResponse(data,content_type = 'applications/json')