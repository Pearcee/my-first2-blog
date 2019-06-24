from django import forms

from .models import feed

class PostForm(forms.ModelForm):

    class Meta:
        model = feed
        fields = ('id', 'author', 'title', 'body', )