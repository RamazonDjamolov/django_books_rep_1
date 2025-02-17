from django import forms

from posts.models import Post


class PostCreatModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'publish', 'status']

        widgets = {
            'publish': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

        def clean_title(self):
            pass