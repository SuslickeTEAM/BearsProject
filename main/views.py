import os
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import Images
import urllib
from django.core.files.storage import FileSystemStorage
import requests
import zipfile



class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


# Скачивание по ссылке
# def links(request):
#     if request.method == 'POST':
#         form = ImagesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view')
#         else:
#             error = 'Форма неверная'
#     form = ImagesForm()
#     data = {
#         'form': form
#     }
#     return render(request, 'upload.html', data)

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        while not uploaded_file.name[-4:] in ['.zip']:
            uploaded_file = request.FILES['document']
            raise TypeError('Это не .zip архив')
        else:
            fs.save(uploaded_file.name, uploaded_file)
            edit(request)
    return render(request, 'upload.html', )


def edit(request):
    try:
        user = 'Users'
        file = os.listdir(path=f'C:/{user}/Suslicke/PycharmProjects/webbear/media')
        print(file[1])
        with zipfile.ZipFile(f'C:/{user}/Suslicke/PycharmProjects/webbear/media/{file[1]}', 'r') as my_zip:
            print(my_zip.namelist())
            my_zip.extractall(f'C:/{user}/Suslicke/PycharmProjects/webbear/media/edit')
        os.remove(f'C:/{user}/Suslicke/PycharmProjects/webbear/media/{file[1]}')
    except FileNotFoundError:
        print('All good')