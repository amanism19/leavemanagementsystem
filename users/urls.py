
from django.urls import path
from . import views

urlpatterns = [   
    path('', views.home, name= 'home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name= 'logout'),
    path('student', views.student, name = 'student'),
    path('mentor', views.mentor, name='mentor')
]
