from django.shortcuts import render
from blog.models import Post, Comment
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"posts": posts})


def blog_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/post.html", context)
