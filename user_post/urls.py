from django.urls import path
from . import views

#here i create the views urls

urlpatterns = [

    path('', views.PostList.as_view(), name='PostList'),
    path('post/<slug:slug>/', views.DetailPost.as_view(), name='DetailPost'),
    path('register/', views.SignUp, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name = 'logout'),
    path('create/', views.CreatePost, name= 'CreatePost')


]