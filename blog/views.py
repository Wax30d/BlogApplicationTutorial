from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.


"""
The post_list view takes the request object as the only parameter.
This parameter is required by all views. 
In this view, you retrieve all the posts with the
published status using the published manager
"""


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    """
    In the
detail view, you use the get_object_or_404() shortcut to retrieve the
desired post. This function retrieves the object that matches the
given parameters or an HTTP 404 (not found) exception if no object
is found.
    """
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish_month=month,
                             publish__day=day
                             )

    return render(request, "blog/post/detail.html", {"post": post})
