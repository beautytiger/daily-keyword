from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('input/', views.keyin, name='input-simple'),
    path('inputf/', views.keyin, name='input-full'),
    path('info/', views.info, name='info'),
    path('infof/', views.info, name='infof'),
    path('cloud/', views.cloud, name='cloud'),
]