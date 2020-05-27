from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
import time
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from login.models import User

# Create your views here.


def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    if request.method == 'POST':# 註冊
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 對密碼進行加密
        password = make_password(password)
        User.objects.create(user_name=name, user_passwd=password,)
        return HttpResponseRedirect('/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        # 如果登入成功，繫結引數到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 查詢使用者是否在資料庫中
        if User.objects.filter(user_name=name).exists():
            user = User.objects.get(user_name=name)
            if check_password(password, user.user_passwd):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 獲取隨機的字串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 繫結令牌到cookie裡面
                # response = HttpResponse()
                response = HttpResponseRedirect('/stu/index/')
                # max_age 存活時間(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服務端
                user.user_ticket = ticket
                user.save()  # 儲存
                return render(request , 'index.html')
            else:
                # return HttpResponse('使用者密碼錯誤')
                return render(request, 'login.html', {'password': '使用者密碼錯誤'})
        else:
            # return HttpResponse('使用者不存在')
            return render(request, 'login.html', {'name': '使用者不存在'})