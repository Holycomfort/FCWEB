from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from .form import UserLogin, UserRegister, BlogForm, UploadFileForm
from .models import User, Message, Blog, UploadFile


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
                return render(request, 'register_page.html', {'error': '用户名已存在', 'form': form})
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request, 'register_page.html', {'error': '两次输入的密码不一致！', 'form': form})
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
    players = User.objects.all()
    return render(request, 'user_page.html', {'user': user, 'players': players})


def notice_request(request, uid):
    user = User.objects.get(id=uid)
    msgs = Message.objects.all()
    return render(request, 'notice_page.html', {'msgs': msgs, 'username': user.username})


def upload_request(request, uid):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            user_id = uid
            uploadfile = UploadFile.objects.create(name=name, file=file, user_id=user_id)
            uploadfile.save()
            return HttpResponseRedirect('/user' + str(uid) + '/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})


def writeblog_request(request, uid):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user_id = uid
            blog = Blog.objects.create(title=title, content=content, user_id=user_id)
            blog.save()
            return HttpResponseRedirect('/user' + str(uid) + '/')
    else:
        form = BlogForm()
    return render(request, 'writeblog_page.html', {'form': form})


def visit_request(request, uid, vid):
    if uid != vid:
        u = User.objects.get(id=uid)
        v = User.objects.get(id=vid)
        blogs = Blog.objects.filter(user_id=vid)
        files = UploadFile.objects.filter(user_id=vid)
        return render(request, 'visit_page.html', {'u': u, 'v': v, 'blogs': blogs, 'files': files})
    else:
        user = User.objects.get(id=uid)
        blogs = Blog.objects.filter(user_id=uid)
        files = UploadFile.objects.filter(user_id=uid)
        return render(request, 'manage_page.html', {'user': user, 'blogs': blogs, 'files': files})


def delete_request(request, uid, id, type):
    if type == "blog":
        blog = Blog.objects.get(id=id)
        blog.delete()
        return HttpResponseRedirect('/user' + str(uid) + '/visit' + str(uid) + '/')
    if type == "file":
        file = UploadFile.objects.get(id=id)
        file.delete()
        return HttpResponseRedirect('/user' + str(uid) + '/visit' + str(uid) + '/')


def download_request(request, id):
    file = UploadFile.objects.get(id=id).file
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="' + str(file) + '"'
    return response
