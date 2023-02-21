from django.contrib import admin
from crm.models import Author, Book, Publisher, Store, Quotes


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("name", "age", "show_avg_price")
	search_fields = ("name",)
	list_per_page = 20

	def show_avg_price(self, obj):
		from django.db.models import Avg
		result = Book.objects.filter(authors=obj).aggregate(Avg("price"))
		return result["price__avg"]

	def __str__(self):
		return f"{self.name}"


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ("name",)
	search_fields = ("name", )
	list_per_page = 20


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("name", "rating", "get_author")
	list_filter = ("rating", "pubdate")
	list_display_links = ('name', "get_author")
	search_fields = ("name", "rating", "authors__name")
	date_hierarchy = "pubdate"
	list_per_page = 20

	def query_set(self, request):
		qs = super().get_queryset(request)
		return qs.prefetch_related('name')
	# Get single value

	def get_author(self, obj):
		return list(obj.authors.all().values_list("name", flat=True))


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ("name", "get_books")
	search_fields = ("name", "books__name")
	list_per_page = 20
	autocomplete_fields = ["books"]

	def query_set(self, request):
		qs = super().get_queryset(request)
		return qs.prefetch_related('books')
	# Get single value

	def get_books(self, obj):
		return list(obj.books.all().values_list("name", flat=True))


@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
	list_display = ("author",)
	list_per_page = 20
