from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^questions/$', views.QustionsList.as_view(), name='questions')
]