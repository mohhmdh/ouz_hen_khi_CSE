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
   
     if request.user.is_authenticated:
        cards = card.objects.filter(user=request.user)  # Get all cards for the logged-in user
        return render(request,'mycard.html' ,{'cards':cards})    
     else:
        cards = []
    
     return render(request,'mycard.html' ,{'cards':cards}) 
    


def create_card(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            card_n = request.POST['card_n']
            e_date = request.POST['e_date']
            cvv = request.POST['cvv']

            # Create the card and associate it with the logged-in user
            cardss = card.objects.create(
                user=request.user,
                card_n=card_n,  # Use card_n from model
                e_date=e_date,  # Use e_date from model
                cvv=cvv  # Use cvv from model
            )
            cardss.save()
            return redirect('mycard')  # Redirect to the page where cards are listed
        else:
            return redirect('signin')  # Redirect to login page if user is not authenticated
    else:
        return render(request, 'createcard.html')
    
    
    
    
