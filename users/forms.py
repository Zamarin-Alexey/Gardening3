from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
#widget=forms.
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
