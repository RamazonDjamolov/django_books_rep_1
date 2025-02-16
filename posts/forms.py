from django import forms

from posts.models import Post


class PostCreatModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish', 'status']
