from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage


# Create your views here.

#def blog_view(request, cat_name=None, author_username=None):
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now())
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    post = get_object_or_404(posts, pk=pid)
    prev_post = posts.filter(id__lt=post.id).order_by('-id').first()
    next_post = posts.filter(id__gt=post.id).order_by('id').first()
    post.counted_view += 1  
    post.save()
    context = {'post': post, 'prev_post': prev_post, 'next_post':next_post}
    return render(request,'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    posts = posts.filter(category__name = cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context = context)

def blog_search(request):
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    if request.method == 'GET':
        #print(request.GET.get('s'))
        if S := request.GET.get('s'):
            posts = posts.filter(content__contains = S)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'test.html', context)