# < boardapp/views.py >

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index) # views.py의 index함수와 연결
]