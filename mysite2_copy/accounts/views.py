from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from .forms import EmailCreationForm, EmailOrUsernameAuthenticationForm



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = EmailOrUsernameAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username')  # This can be username or email
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username_or_email, password=password)
                if user is not None:
                    login(request, user)
                    #next_page = request.GET.get('next')
                    #return redirect(next_page if next_page else '/')
                    return redirect('/')
        form = EmailOrUsernameAuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
    
# Create your views here.
#def login_view(request):
#    if not request.user.is_authenticated:
#        if request.method == 'POST':
#            form = AuthenticationForm(request=request, data = request.POST)
#            if form.is_valid():
#                username = form.cleaned_data.get('username')
#                password = form.cleaned_data.get('password')
#                user = authenticate(request, username = username, password = password)
#                if user is not None:
#                    login(request, user)
#                    return redirect('/')
#        form = AuthenticationForm()
#        context = {'form': form}
#        return render(request,'accounts/login.html', context)
#    else:
#        next_page = request.GET.get('next')
#        if next_page:
#            return redirect(next_page)
#        else:
#            return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = EmailCreationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=True)
                instance.email = form.cleaned_data.get('email')  # Assuming there's an email field in the form
                instance.save()
                print(form.__dict__)
                return redirect('/')
            else:
                print(form.errors)
        form = EmailCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')