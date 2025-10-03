from django.contrib import admin
from .models import Author, Category, Book

# Register the models with the admin site.

# Custom administration for the Book model to show more fields
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'published_date')
    # Add a filter sidebar
    list_filter = ('published_date', 'categories')
    # Add a search box
    search_fields = ('title', 'author__name')
    # Improves the display of the many-to-many field (categories) on the Book form
    filter_horizontal = ('categories',) 

# Register the models
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
