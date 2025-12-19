# This file defines the URL patterns for the LittlelemonAPI app.
# It is included in the main urls.py file of the project.

from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:pk>/', views.single_menu_item),
]