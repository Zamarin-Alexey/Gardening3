from django import forms


class AddPlantForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Описание')
    conditions = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}), label='Условия')
    period_start = forms.DateField(input_formats=['%d/%m'], label="Начало посадки")
    period_finish = forms.DateField(input_formats=['%d/%m'], label="Конец посадки")
    images = forms.ImageField(required=False, label=u'Фотографии',
                              widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    tags = forms.CharField(max_length=255)