from django.shortcuts import render, get_object_or_404
from .models import Book, Category

# Modified view to accept an optional category_id for filtering
def library_view(request, category_id=None):
    app_name = "Django Library Application"
    
    # 1. Fetch all categories (always needed for the navigation list)
    all_categories = Category.objects.all().order_by('name')

    # 2. Filtering Logic
    if category_id:
        # If a category ID is provided in the URL, filter the books
        category = get_object_or_404(Category, pk=category_id)
        # Filter books that have this category, ordered by published date descending
        all_books = Book.objects.filter(categories=category).select_related('author').prefetch_related('categories').order_by('-published_date')
        filter_title =  category.name
    else:
        # Otherwise, show all books, ordered by published date descending
        all_books = Book.objects.select_related('author').prefetch_related('categories').all().order_by('-published_date')
        filter_title = "All Books"

    context = {
        'app_name': app_name,
        'categories': all_categories,
        'books': all_books,
        'filter_title': filter_title,
        'current_category_id': category_id, # Used to highlight the active filter button
    }

    return render(request, 'library/book_list.html', context)
