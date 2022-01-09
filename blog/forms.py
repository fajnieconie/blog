from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')

        widgets = {
            'Tytul': forms.TextInput(),
            'Komentarz': forms.Textarea(),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'image', 'status', 'tags')

        widgets = {
            'Tytul': forms.TextInput(),
            'Alias': forms.TextInput(),
            'Treść': forms.Textarea(),
            'Zdjęcie': forms.ImageField(),
            'Status': forms.ChoiceField(),
            'Tagi': forms.TextInput()
        }
