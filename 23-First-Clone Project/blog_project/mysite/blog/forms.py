from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            "title": forms.TextInput(attrs={"class":"textinputclass"}),
            "text": forms.Textarea(atrrs="class": "editable meduim-editor-textarea postcontent"),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('auther', 'text')

        widgets = {
            "title": forms.TextInput(attrs={"class":"textinputclass"}),
            "text": forms.Textarea(atrrs="class": "editable meduim-editor-textarea"),
        }