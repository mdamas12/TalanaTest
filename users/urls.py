from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views

urlpatterns = [
 
    path(r'winner/', views.winnerView.as_view()),   
    path(r'change/<str:email>/', views.UserChangePassword.as_view()),
    url(r'^', views.UserView.as_view()), 
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
