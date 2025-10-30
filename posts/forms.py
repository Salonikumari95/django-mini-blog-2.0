from django import forms
from .models import Post

# Blog form create/edit ke liye
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
