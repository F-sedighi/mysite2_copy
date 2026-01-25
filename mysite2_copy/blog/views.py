from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from blog.forms import CommentForm
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submited')
            
    posts = Post.objects.filter(status = 1, published_date__lte = timezone.now())
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id, approved=True).order_by('created_date')
        form = CommentForm()
        prev_post = posts.filter(id__lt=post.id).order_by('-id').first()
        next_post = posts.filter(id__gt=post.id).order_by('id').first()
        post.counted_view += 1  
        post.save()
        context = {'post': post, 'comments': comments, 'form': form, 'prev_post': prev_post, 'next_post':next_post}
        return render(request,'blog/blog-single.html', context)
    else:
        return redirect('/accounts/login')
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