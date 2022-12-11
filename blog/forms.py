from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
    tags = forms.CharField(required=False, max_length=255, label='Теги')
    images = forms.ImageField(required=False, label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

class AddPlantForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    conditions = forms.DateInput() (widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Условия')
    planting_period = forms.CharField(max_length=255, verbose_name='Период посадки')
    images = forms.ImageField(required=False, label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

 conditions = models.TextField(verbose_name='Условия')
    planting_period = models.CharField(max_length=255, verbose_name='Период посадки')
    tags = models.CharField(max_length=255)