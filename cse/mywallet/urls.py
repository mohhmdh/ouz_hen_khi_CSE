from django.urls import path
from . import views


urlpatterns = [
    path('mywallet/',views.mywallet,name='mywallet'),
]
