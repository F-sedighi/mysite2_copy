from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


# Create your views here.
def index_view(request):
    #return HttpResponse('hello')
    posts = Post.objects.filter(status = 1).order_by('published_date')
    context = {'posts': posts}
    return render(request,'website/index.html', context = context)

def about_view(request):
    return render(request,'website/about.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def contact_view(request):
    return render(request,'website/contact.html')