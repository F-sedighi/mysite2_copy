from django import forms
from .models import Contact, Newsletter


class NameForm(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    subject = forms.CharField(max_length= 255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    #last_name = forms.CharField(max_length=255)
    #captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['name']
        widget ={
            "subject": forms.Widget.is_required
        }
         
        

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"
