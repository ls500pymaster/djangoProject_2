from django.urls import path
from . import views

urlpatterns = [
    path('', views.crm_main, name='crm'),
    path('authors/', views.authors_all, name='authors_all'),
    path('authors/<pk>/', views.author_solo, name='author_solo'),
    path('publishers/', views.publishers_all, name='publishers_all'),
    path('publishers/<pk>', views.publisher_solo, name='publisher_solo'),
    path('books/', views.books_all, name='books_all'),
    path('books/<book_id>/', views.book_solo, name='authors'),
    path('stores/', views.stores_all, name='stores_all'),
    path('stores/<pk>', views.store_solo, name='store_solo')
]
