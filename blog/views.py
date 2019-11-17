from django.shortcuts import render
from .models import BlogArticles
# Create your views here.
# 基于视图的函数
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html",{"blogs":blogs})