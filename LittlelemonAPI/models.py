# This file defines the data models for the LittlelemonAPI app.
# A data model is a Python class that represents a table in the database.
# Each attribute of the class represents a column in the table.
# Django's Object-Relational Mapper (ORM) uses these models to interact with the database.

from django.db import models  # Django ORM base models

class Category(models.Model): # A data model for a category of menu items
    slug = models.SlugField() # A field for the category slug (e.g., "pizzas")
    title = models.CharField(max_length=255) # A field for the category title (e.g., "Pizzas")

    def __str__(self): # This method returns a string representation of the Category object.
        return f'{self.title}' # Return the title of the category

# Simple data model for a menu item (used by the API)
# This class defines the structure of a menu item in the database.
class MenuItem(models.Model): # A data model for a menu item
    # The title of the menu item, stored as a character field with a maximum length of 255 characters.
    title = models.CharField(max_length=255)  # name of the menu item
    # The price of the menu item, stored as a decimal field with a maximum of 6 digits and 2 decimal places.
    price = models.DecimalField(max_digits=6, decimal_places=2)  # price (e.g., 9.99)
    # The number of items in stock, stored as a small integer field.
    inventory = models.SmallIntegerField()  # how many are available in stock
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) # A foreign key to the Category model

    # This method returns a string representation of the MenuItem object.
    # It is used in the Django admin interface and when printing the object.
    def __str__(self): # This method returns a string representation of the MenuItem object.
        return f'{self.title} : {str(self.price)}' # Return the title and price of the menu item
