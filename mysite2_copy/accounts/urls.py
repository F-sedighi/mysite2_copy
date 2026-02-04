from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    #login
    path('login/', views.login_view, name= 'login'),
    #logout
    path('logout', views.logout_view, name = 'logout'),
    #signup
    path('signup',views.signup_view, name = 'signup'),

    # Password reset urls for built-in function

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),#Displays a form for the user to enter their email address (for requesting a password reset).
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),#Displays a confirmation message that the password reset link has been sent.
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),#This is the form where the user will reset their password after clicking the link in their email.
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),#Displays a confirmation that the password has been successfully reset.
    #path('login', auth_views.LoginView.as_view(), name = 'login'),
    
    # Password reset urls for custom function

    #path('password_reset/', views.password_reset_request, name = 'password_reset'),
    #path('password_reset/done/', views.password_reset_done, name = 'password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.password_reset_confirm, name = 'password_reset_confirm'),
    #path('reset/done/', views.password_reset_complete, name = 'password_reset_done'),
]