from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('migrate', views.migrate, name='migrate'),
    path('display', views.display, name='display'),
]