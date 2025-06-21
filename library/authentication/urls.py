from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('user/', views.user_list, name='user_list'),
    path('user/<int:user_id>/edit/', views.edit_user_view, name='edit_user'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]
