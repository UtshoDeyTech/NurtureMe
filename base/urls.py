from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('survey/', views.survey, name='survey'),
    path('room/<str:pk>/',views.room, name='room'),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout')
]
