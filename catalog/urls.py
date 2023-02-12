from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path("triangle/", views.triangle),
    # path("triangle/result/", views.triangle, name='triangle_result'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:pk>/edit', views.author_edit, name='author_edit'),
    path('post/new/', views.triangle, name='triangle_form'),
]
