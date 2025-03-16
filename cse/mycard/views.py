from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import card
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
                    messages.info(request,'email already exists')
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
    if request.method == 'POST' :
        email = request.POST['email']
        password = request.POST['password1']
        
        user = auth.authenticate(username=email,password=password)
        
        if user is not  None :
            auth.login(request,user)
            return redirect('/mycard')
        else :
            messages.info(request, 'crendentials not invalid ')
            return redirect('signin')
            
                
    else :     
            return render(request,'signin.html')
        
        
        
def mycard(request) :
    cards=card.objects.all()
    
    return render(request,'mycard.html' ,{'cards':cards})       