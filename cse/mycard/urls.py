from django.urls import path
from . import views 

urlpatterns = [
    path('',views.signin,name='signin'),
     path('signup/',views.signup,name='signup'),
     path('signin/',views.signin,name='signin'),
     path('mycard/',views.mycard,name='mycard'),
     path('create_card/',views.create_card,name='create_card'),
     
]
