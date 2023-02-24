from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from django.urls import path
from crm import views
from crm.views import AuthorListView, AuthorDetailView, AuthorCreate, AuthorUpdate, AuthorDelete, PublisherListView, \
    PublisherDetailView, BookListView, IndexView

app_name = 'crm'

urlpatterns = [
    path('', cache_page(60 * 15)(IndexView.as_view()), name='index_crm'),
    # path('', IndexView.as_view(), name='index_crm'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),

    path("author/create/", AuthorCreate.as_view(), name="author_create"),
    path("author/<int:pk>/update/", AuthorUpdate.as_view(), name="author_update"),
    path("author/<int:pk>/delete/", AuthorDelete.as_view(), name="author_delete"),

    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),

    path('books/', BookListView.as_view(), name='book_list'),
    # path('books/', views.get_all_books, name='get_all_books'),
    path('books/<book_id>/', views.get_book_object, name='get_book_object'),

    path('stores/', views.get_all_stores, name='get_all_stores'),
    path('stores/<pk>/', views.get_store_object, name='get_store_object'),

    path("feedback/", views.schedule_email_view, name="feedback"),
    path("feedback/success/", views.send_success_email, name="success"),
    path("feedback/error/", views.feedback_error, name="feedback_error"),
]
