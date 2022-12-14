from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='Заголовок')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
    tags = forms.CharField(required=False, max_length=255, label='Теги')
    images = forms.ImageField(required=False, label=u'Фотографии',
                              widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'images']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']
        widgets = {
            'body': forms.Textarea(attrs={'rows':1}),
        }
