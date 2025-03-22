from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import wallet

# Create your views here.


def mywallet(request):
     if request.user.is_authenticated:
        funds = wallet.objects.filter(user=request.user)  # Get all cards for the logged-in user
        return render(request,'mywallet.html' ,{'funds':funds})    
     else:
        funds = []
     return render(request,'mywallet.html',{'funds':funds})
