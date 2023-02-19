from django.urls import path

from . import views
# from .views import SuccessView

app_name = 'crm'

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

    path("feedback/", views.schedule_email_view, name="feedback"),
    path("feedback/success/", views.send_success_email, name="success"),

    path("scraper/", views.quote_scraper, name="quote_scraper"),
]
