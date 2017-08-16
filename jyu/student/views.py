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
        request.session['scrapyMsg'] = result
        return JsonResponse({'rtnMsg': '绑定成功！', 'rtnCode':'2000'})
    else:
        return JsonResponse({'rtnMsg': '账户名或密码错误，绑定失败！', 'rtnCode':'9000'})

#注销
def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/login')

#首页
def home(request):
    return render(request,'student/index.html')

def score(request):
    return render(request, 'student/score.html')
    #爬取成绩页面的token
    # username = request.session['user']
    # scrapyMsg = request.session['scrapyMsg']
    # result = scrapy.loadScorePage(username, scrapyMsg['xm'], scrapyMsg['url'])
    # if not result:
    #     return JsonResponse({'rtnMsg': '获取历年成绩失败！', 'rtnCode': '9000'})
    # else:
    #     scoreList = scrapy.loadlncj(result['viewstate'], result['scoreurl'],result['header'])
    #     if not result:
    #         return JsonResponse({'rtnMsg': '获取历年成绩失败！', 'rtnCode': '9000'})
    #     else:
    #         return JsonResponse({'rtnMsg': '获取历年成绩成功！', 'rtnCode': '2000', 'data': scoreList})