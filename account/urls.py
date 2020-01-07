# -*- coding: utf-8 -*-
# @Time : 2020/1/7 15:20
# @Author : wangmengmeng
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
]
