# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
import json
from django.http import HttpResponse

# Create your views here.
class jsonCBV(View):
    # def get(self,request,*args,**kwargs):
    #     # emp_data = {
    #     #     'eno':100,
    #     #     'ename':'sunny',
    #     #     'esal':1000,
    #     #     'eaddr':'mumbhai',
    #     # }
    #     json_data = json.dumps({'msg':'this new msg'})
    #     # return JsonResponse(emp_data)
    #     return HttpResponse(json_data,content_type='application/json')
    # def update(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'this new msg'})
    #     return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'tposthis new msg'})
        return HttpResponse(json_data,content_type='application/json')

    # def put(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'this new msg'})
    #     return HttpResponse(json_data,content_type='application/json')
