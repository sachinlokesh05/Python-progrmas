# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.
def emp_data_view(request):
    emp_data = {
        'eno':100,
        'ename':'sunny',
        'esal':10000,
        'eaddr':'mumbhai',
    }
    json_data = json.dumps(emp_data)
    resp = '<h1>Employee Number :{} <br>  Employee ename :{} <br>  Employee sal :{} <br>  Employee addres : {}</h1> '.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp )



def emp_data_viewjson(request):
    emp_data = {
        'eno':100,
        'ename':'sunny',
        'esal':10000,
        'eaddr':'mumbhai',
    }
    json_data = json.dumps(emp_data)
    # return HttpResponse(json_data, content_type = 'application/json' )
    return JsonResponse(emp_data)


 

