from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    x = request.POST.get('user_name')
    print(x)
    return render(request,'login/login.html',{'name':'adel101'})