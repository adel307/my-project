from django.shortcuts import render
from .forms import Market_login

# Create your views here.

def market_login(request):

    return render(request,'market_login/market_login.html',{'lf':market_login})
