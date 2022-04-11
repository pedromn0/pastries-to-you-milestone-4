from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CommentsForm, PostForm
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

@login_required
def add_post(request):
    """
    Add a new post to blog
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners \
             can have access to that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            form.instance.post_user = user
            post = form.save()
            messages.success(request, 'New post added')
            return redirect('blog_view')
        else:
            messages.error(request, 'Failed to add new post. \
                 Please ensure that all data was filled correctly.')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit post from Blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can \
            have access to that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            form.instance.post_user = user
            post = form.save()
            messages.success(request, 'Post Updated')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update this post. \
                 Please ensure that all data was filled correctly.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.slug}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Delete a post from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can have access to that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect(('blog_view'))
