from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
    tags = forms.CharField(required=False, max_length=255, label='Теги')
    images = forms.ImageField(required=False, label=u'Фотографии',
                              widget=forms.FileInput(attrs={'multiple': 'multiple'}))

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']
        widgets = {
            'body': forms.Textarea(attrs={'rows':1}),
        }

# class AddPlantForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Название')
#     body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
#     conditions = forms.DateInput(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Условия')
#     planting_period = forms.CharField(max_length=255, verbose_name='Период посадки')
#     images = forms.ImageField(required=False, label=u'Фотографии',
#                               widget=forms.FileInput(attrs={'multiple': 'multiple'}))
#     conditions = forms.CharField(verbose_name='Условия')
#     planting_period = forms.CharField(max_length=255, verbose_name='Период посадки')
#     tags = forms.CharField(max_length=255)
