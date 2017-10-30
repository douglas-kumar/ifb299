from django.contrib.auth.models import User
from django import forms

from .models import Favorite


class FavoriteForm(forms.ModelForm):

    class Meta:
        model = Favorite
        exclude = (
            'content_type', 'object_id', 'content_object', 'count')

ACCOUNT_TYPES = [
    ('TOURIST', 'Tourist'),
    ('STUDENT', 'Student'),
    ('BUSINESS', 'Business'),
]

INFO_TYPES = [
    ('0', 'College'),
    ('9', 'All'),
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

SORTING_OPTIONS = {
    ('name','Name Ascending'),
    ('-name','Name Descending'),
}

class SearchForm(forms.Form):
    search_name = forms.CharField(widget=forms.TextInput)
    info_type = forms.ChoiceField(choices=INFO_TYPES, required=True)
    sorting_options = forms.CharField(widget=forms.RadioSelect(choices=SORTING_OPTIONS))
