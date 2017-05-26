# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Blog, Comment, User

def index(request):
    context = {
    "blogs" : Blog.objects.all()
    # select * From Blog
    #select * from Blogs
    }
    return render(request, "test_app/index.html", context)


def blogs(request):
    # using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    # insert into BLog (title, blog, created_at, updated_at)) values (title, blog, now(), now() )
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog=blog)
    return redirect('/')

def userorm(request):
    users = User.objects.filter(age__lt=70)|User.objects.filter(first_name__startswith="S")
    context = {"users":users}
    return render(request,"test_app/userorm.html",context)

# Create your views here.
