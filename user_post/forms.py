from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    '''
    this django form class is for creating signup form to sign up users
    here i used django usercreation form
    '''
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        '''
        here is the class meta for defining which model & form fields is used to store form data
        '''

        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', )


class PostForm(forms.ModelForm):
    '''
    this is also form class to create post form from which user can write a post
    '''

    class Meta:
        '''
        this class meta used exclude to exclude form fields and labels to give form fields label
        '''
        model = Post
        fields = ['title', 'text', 'slug', ]
        exclude = ['user', ]

        labels = {
            'title': ('Title'),
            'text': ('Text'),
            'slug': ('Slug'),
            }

        help_texts = {
            'slug': 'use words separated by hyphens ex; format-of-post',
        }



