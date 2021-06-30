from django.urls import path
from .views import BaseView
from .views import links, download

urlpatterns = [
    path('', BaseView.as_view(), name='main'),
    path('upload/', links, name='upload'),
    path('unloading/', download, name='unloading')
    # path('unload', unload.as_view(), name='main'),
]
