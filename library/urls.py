from django.urls import path
from . import views

urlpatterns = [
    # 1. The main page route (shows all books)
    path('', views.library_view, name='book_list'),
    
    # 2. The filter route (This is where you put the logic for filtering by category ID)
    path('category/<int:category_id>/', views.library_view, name='filter_by_category'),
]
