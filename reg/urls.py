from django.urls import path

from . import views

urlpatterns = [
    path('r', views.index, name='merr'),
    path('s', views.Service, name='merr'),
    path('', views.Regis, name='regjistro'),
]
