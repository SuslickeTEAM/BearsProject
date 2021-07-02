from django.urls import path
from .views import BaseView
from .views import upload, edit

urlpatterns = [
    path('', upload, name='upload'),
    path('view/', edit, name='view'),
    # path('unload', unload.as_view(), name='main'),
]
