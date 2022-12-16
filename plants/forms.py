from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    estimation = forms.IntegerField(max_value=5, min_value=0)
    title = forms.CharField(max_length=255, label='Заголовок рецензии')
    body = forms.CharField(widget=forms.Textarea(), label='Текст рецензии')


    class Meta:
        model = Review
        fields = ['title', 'body', 'estimation']