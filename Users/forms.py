from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    website = forms.CharField()
    twitter = forms.CharField()
    linkedin = forms.CharField()
    facebook = forms.CharField()
    class Meta:
        model = Profile
        fields = ['image', 'website', 'twitter', 'linkedin', 'facebook']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['website'].required = False
        self.fields['twitter'].required = False
        self.fields['linkedin'].required = False
        self.fields['facebook'].required = False