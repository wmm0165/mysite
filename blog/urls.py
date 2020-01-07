# -*- coding: utf-8 -*-
# @Time : 2020/1/6 14:35
# @Author : wangmengmeng
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    path('<int:article_id>/', views.blog_article, name='blog_article'),
]
