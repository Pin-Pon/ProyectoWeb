from django.shortcuts import render
from blog.models import Post
from django.contrib.admin import *
# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})