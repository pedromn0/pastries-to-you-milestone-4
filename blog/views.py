from django.shortcuts import render, get_object_or_404

from .models import Post, Comments

# Create your views here.


def blog_view(request):
    """
    Render all blogs available
    """
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)
