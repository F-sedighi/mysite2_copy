from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now())
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)

def blog_single(request, pid):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, pk=pid)
    post.counted_view += 1
    post.save()
    print(post.counted_view)
    context = {'post': post}
    return render(request,'blog/blog-single.html', context)

def test(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'test.html', context)