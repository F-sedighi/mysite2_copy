from django import forms
from .models import Contact, Newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    subject = forms.CharField(max_length= 255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    #last_name = forms.CharField(max_length=255)
    captcha = CaptchaField()
    subject = forms.CharField(required=False,
                              max_length=255,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Enter subject'}
                                  )
                            )
    class Meta:
        model = Contact
        fields = ['email', 'subject', 'message'] 
         
    def clean(self):
        cleaned_data = super().clean()
        # You can add additional checks here to skip validation for empty fields
        if not cleaned_data.get('subject'):  # If it's empty, no validation error
            cleaned_data['subject'] = None
        return cleaned_data
         
    
        

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"
