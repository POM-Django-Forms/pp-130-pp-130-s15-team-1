from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('create/', views.create_book_view, name='book_create'),
    path('filter/', views.filter_books, name='filter_books'),
    path('user/<int:user_id>/', views.user_books, name='user_books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/edit/', views.update_book_view, name='book_update'),
]