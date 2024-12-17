from django.shortcuts import render
from page.models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,"blog/post/list.html",context={"posts":posts})
