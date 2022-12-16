from django.contrib.auth.forms import UserCreationForm
from django import forms

from base import views
from .models import User, Member
from django.core import validators
from django.contrib.auth import get_user_model



class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # import get_user_model to have access to Manager
        User = get_user_model()
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        exclude = ['host']