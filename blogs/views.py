from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

def home(request):
    '''home page views'''
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}

    return render(request, 'blogs/home.html', context)

def new_post(request):
    '''post new content'''
    if request.method != 'POST':
        # No data was submitted; create a blank form
        form = BlogPostForm()
    else:
        # POST data submitted; process data
        form = BlogPostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:home'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def post(request, post_id):
    """single post page"""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}

    return render(request, 'blogs/post.html', context)

def edit_post(request, post_id):
    '''Edit a single post'''
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Initial request; prefill form with the current post
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:home'))

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
