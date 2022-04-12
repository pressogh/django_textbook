# < boardapp/forms.py >

from django import forms
from .models import Post


class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['title', 'content']  # PostForm에서 사용할 Post 모델의 속성