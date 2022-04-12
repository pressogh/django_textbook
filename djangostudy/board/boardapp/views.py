# < boardapp/views.py >

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Comment
from .forms import PostUploadForm

# Create your views here.

def index(request):
    post_list = Post.objects.order_by('-create_time')
    post_dict = {"post_list": post_list}

    return render(request, 'boardapp/posts.html', post_dict)

def PostDetailView(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {'post': post}

    return render(request, 'boardapp/post_detail.html', data)

def PostUploadView(request):
    if request.method == 'GET':
        form = {"form": PostUploadForm()}
        
        return render(request, 'boardapp/post_upload.html', form)

    if request.method == 'POST':
        form = PostUploadForm(request.POST) # request.POST에 있는 데이터를 form에 저장
        if form.is_valid(): # form의 데이터가 정상이라면
            post = form.save(commit=False)  # post에 form의 데이터를 넣어주고
            post.save() # post를 저장
        return redirect('boardapp:index') # 메인 페이지로 이동