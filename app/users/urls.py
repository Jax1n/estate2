from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout')
]