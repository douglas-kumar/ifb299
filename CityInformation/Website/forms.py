from django.contrib.auth.models import User
from django import forms

ACCOUNT_TYPES = [
    ('TOURIST', 'Tourist'),
    ('STUDENT', 'Student'),
    ('BUSINESS', 'Business'),
]

# extend User table to include the user's type
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    account_type = forms.CharField(label='Choose Account Type:',
                                   widget=forms.RadioSelect(
                                       choices=ACCOUNT_TYPES)
                                   )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
