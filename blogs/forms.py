# forms module for blogs app
from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    '''form class for blog post'''
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        label = {'title': '', "text": ""}
        widgets= {'text': forms.Textarea(attrs={'cols': 80})}
