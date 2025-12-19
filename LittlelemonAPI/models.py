# This file defines the data models for the LittlelemonAPI app.
# A data model is a Python class that represents a table in the database.
# Each attribute of the class represents a column in the table.
# Django's Object-Relational Mapper (ORM) uses these models to interact with the database.

from django.db import models  # Django ORM base models

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

# Simple data model for a menu item (used by the API)
# This class defines the structure of a menu item in the database.
class MenuItem(models.Model):
    # The title of the menu item, stored as a character field with a maximum length of 255 characters.
    title = models.CharField(max_length=255)  # name of the menu item
    # The price of the menu item, stored as a decimal field with a maximum of 6 digits and 2 decimal places.
    price = models.DecimalField(max_digits=6, decimal_places=2)  # price (e.g., 9.99)
    # The number of items in stock, stored as a small integer field.
    inventory = models.SmallIntegerField()  # how many are available in stock
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, default=1)

    # This method returns a string representation of the MenuItem object.
    # It is used in the Django admin interface and when printing the object.
    def __str__(self):
        return f'{self.title} : {str(self.price)}'