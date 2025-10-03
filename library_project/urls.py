from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is imported!

urlpatterns = [
    # Admin is necessary for data entry
    path('admin/', admin.site.urls),
    
    # This line sends all requests for the root path ('') to your app's urls.py
    path('', include('library.urls')), 
]
