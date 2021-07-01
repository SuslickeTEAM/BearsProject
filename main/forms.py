from .models import Images
from django.forms import ModelForm, TextInput
from django import forms


# class ImagesForm(ModelForm):
#     class Meta:
#         model = Images
#         fields = ['url']
#
#         widgets = {
#             'url': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Ссылка',
#                                     },)
#         }

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()