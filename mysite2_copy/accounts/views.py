from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from .forms import EmailCreationForm, EmailOrUsernameAuthenticationForm, SetNewPasswordForm
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.urls import reverse
from .forms import PasswordResetRequestForm
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.conf import settings



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
    
def password_reset_request(request):
    form = PasswordResetRequestForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = request.build_absolute_uri(
                reverse('accounts:password_reset_confirm',
                        kwargs={'uidb64': uid, 'token': token}
                )
            )

            context = {
                'user':user,
                'reset_url': reset_url,
                'site_name': 'My Awesome Site',
            }

            subject = 'Reset Password'
            message = render_to_string(
                'registration/password_reset_email.html',
                context
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email]
            )

        return redirect('accounts:password_reset_done')
    return render(request, 'registration/password_reset_form.html', {'form': form})

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    if user is None or not default_token_generator.check_token(user, token):
        return render(request, 'accounts/password_reset_invalid.html')
    
    form = SetNewPasswordForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return redirect('accounts:password_reset_complete')
    
    return render(
        request,
        'accounts/password_reset_confirm.html',
        {'form': form}
    )

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html')