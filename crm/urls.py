from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_all, name='authors_all'),
    # path('author/<int:pk>/edit', views.author_edit, name='author_edit'),
    # path('post/new/', views.triangle, name='triangle_form'),
]
