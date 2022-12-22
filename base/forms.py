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

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'nee_name': forms.TextInput(attrs={'class':'form-control'}),
            'place_of_birth': forms.TextInput(attrs={'class':'form-control'}),
            'place_of_death': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_death': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_marriage': forms.TextInput(attrs={'class': 'form-control'}),
            'spouses': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Spouses'}),
            'parents': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Parents'}),
            'siblings': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Siblings'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes'}),
        }