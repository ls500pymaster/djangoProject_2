from django.urls import path
from . import views

urlpatterns = [
    path('', views.crm_main, name='crm'),
    path('authors/', views.authors_all, name='authors_all'),
    path('publishers/', views.publishers_all, name='publishers_all'),
    path('books/', views.books_all, name='books_all'),
    path('stores/', views.stores_all, name='stores_all'),
]
