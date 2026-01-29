from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",  # New label for clarity
        widget=forms.TextInput(attrs={"autofocus": True})
    )




# Custom validator to ensure unique email
def validate_unique_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError(_("This email is already in use. Please use a different email address."))

class EmailCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        required=True,
        validators=[validate_unique_email]  # Custom email validator
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include email explicitly


