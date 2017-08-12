# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("神州信息")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(c)

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': '自强学堂', 'content': '各种IT技术教程'}
    List = map(str, range(100))  # 一个长度为100的 List
    model = {
        'TutorialList': TutorialList,
        'info_dict':info_dict,
        'List': List
    }
    return render(request, 'yiban/home.html', model)
# Create your views here.
