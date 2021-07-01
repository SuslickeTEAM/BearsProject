from django.urls import path
from .views import BaseView
from .views import upload

urlpatterns = [
    path('', BaseView.as_view(), name='main'),
    path('upload/', upload, name='upload'),
    # path('view/', download, name='view'),
    # path('unload', unload.as_view(), name='main'),
]
