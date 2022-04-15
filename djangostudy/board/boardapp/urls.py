# < boardapp/urls.py >

from django.urls import path
from . import views

app_name = 'boardapp'

urlpatterns = [
    path('', views.index, name="index"), # views.py의 index함수와 연결
    path('<int:post_id>/', views.PostDetailView, name="detail"),   # views.py의 PostDetailView 함수와 연결
    path('post_upload', views.PostUploadView, name="upload"),    # # views.py의 PostUploadView 함수와 연결
    path('<int:post_id>/comment_create/', views.CommentUploadView, name='comment_upload')
]