import datetime
from django.shortcuts import render
from django.views.generic import View
from .forms import ImagesForm
from .models import Images
import urllib
from django.core.files.storage import FileSystemStorage
import requests
import zipfile



class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')


def links(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST)
        if form.is_valid():
            form.save()
            print('ALL GOOD')
        else:
            error = 'Форма неверная'
    form = ImagesForm()
    data = {
        'form': form
    }

    return render(request, 'upload.html', data)


def download(request):
    url = Images.objects.all()
    some_url = url[0]
    address = some_url.url
    print(address)
    r = requests.get(address)

    # with open("C:\Media\medias1.zip", "wb") as code:
    #     code.write(r.content)

    urllib.request.urlretrieve(address, "C:\Media\medias.zip")
    url = Images.objects.all().delete()

    link = {
        'urls': url
    }
    edit(request)
    return render(request, 'unloading.html', link)


def edit(request):
    with zipfile.ZipFile('C:\Media\medias.zip', 'r') as my_zip:
        print(my_zip.namelist())
        my_zip.extractall('C:\Medias')
        # Для нейронки

