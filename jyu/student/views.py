# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import scrapy

# Create your views here.
#登录页面初始化
def login(request):
    if 'user' in request.session:
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'student/login.html', {'name': 'vector'})

#登录处理
def loginPost(request):
    username = request.POST['username']
    password = request.POST['password']
    result = scrapy.login(username, password)
    if result:
        request.session['user'] = username
        request.session['password'] = password
        request.session['url'] = result
        return JsonResponse({'rtnMsg': '绑定成功！', 'rtnCode':'2000'})
    else:
        return JsonResponse({'rtnMsg': '账户名或密码错误，绑定失败！', 'rtnCode':'9000'})

#注销
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        del request.session['url']
    return HttpResponseRedirect('/login')

#首页
def home(request):
    return render(request,'student/index.html')

def score(request):
    #爬取成绩页面的token
    url = request.session['url']
    result = scrapy.loadScorePage(url)
    if not result:
        return render(request, 'student/score.html',{'rtnMsg': '获取历年成绩失败！', 'rtnCode': '9000'})
    else:
        scoreList = scrapy.loadlncj(result['viewstate'], result['url'])
        return render(request, 'student/score.html')
        if not result:
            return render(request, 'student/score.html', {'rtnMsg': '获取历年成绩失败！', 'rtnCode': '9000'})
        else:
            return render(request, 'student/score.html', {'rtnMsg': '获取历年成绩成功！', 'rtnCode': '2000'})