from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now())
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

def test(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'test.html', context)