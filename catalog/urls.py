from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path("triangle/", views.triangle),
    path("triangle/result/", views.triangle, name='triangle_result'),
]