from .models import Images
from django.forms import ModelForm, TextInput


class ImagesForm(ModelForm):
    class Meta:
        model = Images
        fields = ['url']

        widgets = {
            'url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка',
                                    },)
        }