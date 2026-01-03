# This file is the main URL configuration for the Littlelemon project.
# It defines the URL patterns for the entire project.
# A URL pattern is a mapping between a URL and a view function that should be called when that URL is requested.

"""
URL configuration for Littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.contrib import admin
from django.urls import path, include

# The urlpatterns list is a list of URL patterns that Django will try to match against the requested URL.
# When a URL is requested, Django starts at the first pattern in urlpatterns and works its way down the list, comparing the requested URL against each pattern until it finds one that matches.
urlpatterns = [
    # The admin/ URL pattern is for the Django admin site.
    # The admin site is a ready-to-use interface for managing your site's content.
    path('admin/', admin.site.urls),
    # The api/ URL pattern includes the URL patterns from the LittlelemonAPI app.
    # This is a good practice for organizing your project's URLs.
    # Each app can have its own urls.py file, and you can include them in the main urls.py file.
    path('api/', include('LittlelemonAPI.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]