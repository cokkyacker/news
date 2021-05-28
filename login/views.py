import hashlib
import os
import time

from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from lib.lib import my_md5
from login.models import Users, UserInfo


def login(request):
    if request.session.get("username"):
        return redirect("/login/index/")
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        # if username == 'admin' and password == "123":

        # md5 = hashlib.md5()
        # md5.update(password.encode())
        # pw = md5.hexdigest()

        pw = my_md5(password)
        rs = Users.objects.filter(username=username, password=pw)
        print(rs)
        if rs:
            request.session['username'] = username
            request.session['userid'] = rs[0].id
            return HttpResponse("1")
        else:
            return HttpResponse("2")


def index(request):
    if request.session.get("username"):
        return render(request, 'index.html')
    else:
        return redirect("/login/denglu/")


def welcome(request):
    return render(request, 'welcome.html')


def exit(request):
    del request.session['username']
    del request.session['userid']
    return redirect('/login/denglu/')


def init(request):
    users = Users()
    users.username = "admin222"

    # md5 = hashlib.md5()
    # md5.update('初始化完成！'.encode())
    # pw = md5.hexdigest()
    pw = my_md5("222")
    users.password = pw
    users.save()
    return HttpResponse("初始化完成！")

class UserInfoForm(forms.Form):
    nickname = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-text'}),
        error_messages={
            'max_length': "最大长度不能超过64位",
            'requried': '不能为空'
        }
    )
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'input-text'}),
        error_messages={
            'invalid': '必须输入电子邮箱格式'
        }
    )
    birthday = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                'class': "input-text",
                'onclick': "WdatePicker()"
            }),
        error_messages={
            'invalid': '%Y-%m-%d格式进行录入'
        }
    )
    thumb = forms.FileField(
        required=False,
        max_length=128,
        widget=forms.FileInput(attrs={'accept': '.jpg,.png'})
    )
    gender = forms.IntegerField(
        required=True,
        widget=forms.Select(
            attrs={'class':'select'},
            choices=((1, '男'), (2, '女'))
        ),
        error_messages={
            'required': '性别必须选择'
        }
    )
    hobby = forms.MultipleChoiceField(
        required=True,
        choices=((1, '上网'), (2, '旅游'), (3, '读书')),
        widget=forms.CheckboxSelectMultiple(),
        error_messages={
            'required': '爱好必须选择'
        }
    )
    pos = forms.IntegerField(
        required=True,
        widget=forms.RadioSelect(choices=((1, "国内"), (2, "国外"))),
        error_messages={
            'required': '位置必须选择'
        }
    )




def userinfo(request):
    if request.method == 'GET':
        userInfoForm = UserInfoForm()
        userInfoForm.initial['hobby'] = [2,3]
        userInfoForm.initial['pos'] = [1,]
        return render(request, 'user-info.html', {'userInfoForm': userInfoForm})
    else:
        userInfoForm = UserInfoForm(request.POST, request.FILES)
        if userInfoForm.is_valid():
            data = userInfoForm.cleaned_data
            ofile = request.FILES['thumb']
            filename = str(int(time.time()))+os.path.splitext(ofile.name)[1]
            tofile = os.path.join('static/upload/', filename)
            f = open(tofile, 'wb')
            for chunk in ofile:
                f.write(chunk)
            f.close()

            data['thumb'] = os.path.join('upload/', filename)
            UserInfo.objects.create(**data)
            print(tofile)
            # print(filename)
            # print(ofile.name)
            # print(data)
            return HttpResponse("ok")
        else:
            print(userInfoForm.errors)
            return render(request, 'user-info.html', {'userInfoForm': userInfoForm})