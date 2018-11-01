from django.shortcuts import render,get_object_or_404
from .models import Post
def index(request):
    posts=Post.objects.order_by('-created_date')
    return render(request,'blogtest1/post_list.html',{'posts':posts})
def show(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    return render(request,'blogtest1/post_detail.html',{'post':post})
