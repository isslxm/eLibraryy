from django.urls import path
from . import views


urlpatterns = [ 
    path('registration/', views.register, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]   