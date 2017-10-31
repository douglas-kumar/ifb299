from django.contrib.auth.models import User
from django import forms

ACCOUNT_TYPES = [
    ('TOURIST', 'Tourist'),
    ('STUDENT', 'Student'),
    ('BUSINESS', 'Business'),
]

INFO_TYPES = [
    ('0', 'College'),
    ('9', 'All'),
]

RATINGS = [
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
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

class ReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=RATINGS, required=True)
    text = forms.CharField(widget=forms.TextInput)