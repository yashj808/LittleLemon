# This file is used to register your models with the Django admin site.
# The Django admin site is a ready-to-use interface for managing your site's content.
# When you register a model with the admin site, you can use the admin site to create, read, update, and delete instances of that model.

from django.contrib import admin
from .models import MenuItem, Category

# The admin.site.register() function is used to register a model with the admin site.
# In this case, we are registering the MenuItem model.
admin.site.register(MenuItem)
admin.site.register(Category)
# Register your models here.