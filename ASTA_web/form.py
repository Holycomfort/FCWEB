from django import forms
from .models import Blog, UploadFile


class UserRegister(forms.Form):
    username = forms.CharField(label='注册用户名', max_length=100)
    password1 = forms.CharField(label='设置密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())


class UserLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title', 'content'}


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = {'name', 'file'}
