from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from core.models import Contact
from core.forms import NameForm, ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = "unknown"
            instance.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited')
    form = ContactForm()
    return render(request,'website/contact.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/') 


def test1_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponse('done')
        else:
            HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test1.html', {'form': form})

#def test1_view(request):
#    if request.method == 'POST':
#        form = NameForm(request.POST)
#        if form.is_valid():
#            name = form.cleaned_data['name']
#            email = form.cleaned_data['email']
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            print(name, email, subject,message)
#            return HttpResponse('done')
#        else:
#            HttpResponse('not valid')
#    form = NameForm()
#    return render(request, 'test1.html', {'form': form})