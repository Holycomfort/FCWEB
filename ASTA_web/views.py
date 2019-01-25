from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .form import UserLogin, UserRegister
from .models import User
from .models import Message

# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():  # 获取表单信息
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                the_user = User.objects.get(username=username, password=password)
                return HttpResponseRedirect('/user' + str(the_user.id) + '/')
            except:
                return render(request, 'login_page.html', {'error': '该用户名不存在！', 'form': form})
    else:
        form = UserLogin()
        return render(request, 'login_page.html', {'form': form})


def register_request(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():  # 获取表单信息
            username = form.cleaned_data['username']
            namefilter = User.objects.filter(username=username)
            if len(namefilter) > 0:
                return render(request, 'register_page.html', {'error': '用户名已存在'},)
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request, 'register_page.html', {'error': '两次输入的密码不一致！'})
                else:
                    # 将表单写入数据库
                    user = User.objects.create(username=username, password=password1)
                    user.save()
                    return HttpResponseRedirect('/user' + str(user.id) + '/')
    else:
        form = UserRegister()
        return render(request, 'register_page.html', {'form': form})


def user_request(request, uid):
    user = User.objects.get(id=uid)
    return render(request, 'user_page.html', {'user': user})


def notice_request(request, uid):
    user = User.objects.get(id=uid)
    msgs = Message.objects.all()
    return render(request, 'notice_page.html', {'msgs': msgs, 'username': user.username})


def upload_request(request, uid):
    user = User.objects.get(id=uid)
    return HttpResponse('hello ' + str(user.username) + ' this page is not yet open...')
