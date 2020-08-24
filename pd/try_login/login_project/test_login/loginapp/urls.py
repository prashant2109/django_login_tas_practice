from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signup_efs/', views.signup_extra_fields, name='sign_up_efs'),
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login_page'),
    path('logout/', views.logout_request, name='logout'),
    path('home/', views.home, name='home'),
]
