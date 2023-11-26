from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_page/', views.register_user, name='register_user'),
    path('login_page/', views.login_user, name='login_user'),
    path('logout_page/', views.logout_user, name='logout_user'),
    path('makepost/', views.makepost, name='makepost'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
]
