from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
]