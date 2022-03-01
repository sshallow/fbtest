from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login.html')


def index(request):
    user = request.POST.get('username', '')
    pwd = request.POST.get('password', '')

    if user == 'admin' and pwd == '123456':
        return HttpResponse('登录成功')
    return HttpResponse('登录失败')
