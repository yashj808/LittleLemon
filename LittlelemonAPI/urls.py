# This file defines the URL patterns for the LittlelemonAPI app.
# It is included in the main urls.py file of the project.

from django.urls import path # Import the path function from Django's URL library
from . import views # Import the views from the current directory

urlpatterns = [ # A list of URL patterns
    path('menu-items/', views.menu_items), # A URL pattern for all menu items
    path('menu-items/<int:pk>/', views.single_menu_item), # A URL pattern for a single menu item, identified by its primary key
    path('categories/', views.categories),  # A URL pattern for all categories
    path('categories/<int:pk>/', views.single_category) # A URL pattern for a single category, identified by its primary key
]
