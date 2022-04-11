from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import CommentsForm
from .models import Post, Comments, UserProfile

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


def blog_detail(request, post_id):
    """
    View each blog Post in detail, commentary 
    and the possibility to create one
    """
    post = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(post_id=post_id).order_by(
        '-comments_date_stamp')

    if request.method == 'POST':
        form = CommentsForm(request.POST)

        if form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            form.instance.comments_user = user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            messages.success(request, 'Comms added to this post')
            return redirect('blog_detail', post_id)

    else:
        form = CommentsForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/blog_detail.html', context)
