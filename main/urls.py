from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_main_page),
    path('videos/', views.video_list, name='videos'),
    path('about/', views.render_about_page, name='about'),
    path('books/', views.render_book_page, name='books'),
    path('books/<int:book_id>/', views.render_one_of_books, name='book_detail'), 
]