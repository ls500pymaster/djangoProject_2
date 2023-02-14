from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_crm, name='index_crm'),
    path('authors/', views.get_all_authors, name='get_all_authors'),
    path('authors/<name>/', views.get_author_object, name='get_author_object'),

    path('publishers/', views.get_all_publishers, name='publishers_all'),
    path('publishers/<pk>/', views.get_publisher_object, name='get_publisher_object'),

    path('books/', views.get_all_books, name='get_all_books'),
    path('books/<book_id>/', views.get_book_object, name='get_book_object'),

    path('stores/', views.get_all_stores, name='get_all_stores'),
    path('stores/<pk>/', views.get_store_object, name='get_store_object'),

    path('celery/', views.generate_celery_form, name='generate_celery_form')
]
