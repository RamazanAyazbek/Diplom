from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms

class UserForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'username',
            'placeholder':('Username'),
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'first_name',
            'placeholder':('First Name')
        }
    )) 
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'last_name',
            'placeholder':('Last Name')
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'type':'email',
            'placeholder':('Email')
        }
    ))
    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder':'Password'
        }
    ))
    password2 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            # 'class':'form-control',
            'placeholder':'Repeat Password'
        }
    ))
    group_choices = (
        ('M','Manager'),
        ('U','User'),
        ('C','Customer'),   
    )
    groups = forms.ChoiceField(choices=group_choices)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2','groups']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]