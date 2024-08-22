from django.urls import path
from . import views
from .views import Signup, Login, DashBoardView

urlpatterns = [
    path('test', views.index),
    path('register/', Signup.as_view(), name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
]