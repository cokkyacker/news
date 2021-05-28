from django.db import models

class UserInfo(models.Model):
    nickname = models.CharField(max_length=64)
    email = models.EmailField(default='')
    birthday = models.DateField()
    thumb = models.CharField(max_length=128, default='')
    gender = models.IntegerField(default=1)
    hobby = models.CharField(max_length=128)
    pos = models.IntegerField(default=1)

class Users(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    userinfo = models.CharField(max_length=100, default='')


