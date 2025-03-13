from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 =request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2 :
                if User.objects.filter(username=username).exists():
                    messages.info(request,'username already exists')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already exusts')
                    return redirect('signup')
                else:
                    user= User.objects.create_user(username=username ,email=email,password=password1) 
                    user.save()
                    print('user created')
                    return redirect('signin')
            else:
                messages.info(request,'password not matching')
                return redirect('signup')
    else:
        return render(request ,'signup.html')
def signin(request):
    return render(request,'signin.html')