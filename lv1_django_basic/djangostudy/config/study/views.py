from django.shortcuts import render
from django.http import HttpResponse    # Http 응답을 반환해주는 함수

# Create your views here.

# HelloView로 요청이 오면
def HelloView(request):
    # Http 응답 반환
    return HttpResponse('Hello World!')