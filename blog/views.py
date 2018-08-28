from django.shortcuts import render

from .models import Post

def index(request):
    blog = Post.objects.all().order_by('-date')
    return render(request,'blog/blog.html',{'blog':blog})