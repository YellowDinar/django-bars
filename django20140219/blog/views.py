from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def index(request):
    return HttpResponse("INDEX.")

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})
    # return HttpResponse("List of posts")

def post(request,post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post.html', {'post':post})

def post_new(request):
    return render(request, 'post_new.html', {})
    # return HttpResponse("Adding new post")

def post_edit(request,post_id):
    return render(request, 'post_edit.html' , {'id' : int(post_id)})

def post_delete(request,post_id):
    return render(request, 'post_delete.html' ,{'id' : int(post_id)})
