# This file is used to write tests for the LittlelemonAPI app.
# Tests are used to check that your code is working correctly.
# Django provides a test framework that allows you to write and run tests for your app.

from django.test import TestCase
from .models import MenuItem

# The TestCase class is a subclass of the standard Python unittest.TestCase class.
# It provides a number of additional assertion methods that are useful for testing web applications.
class MenuItemTest(TestCase):
    # The setUp method is called before each test method is run.
    # It is used to set up any objects that are needed for the tests.
    def setUp(self):
        MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        MenuItem.objects.create(title="Cake", price=100, inventory=50)

    # Test methods must start with the word 'test'.
    def test_get_item(self):
        # The get() method is used to retrieve a single object from the database.
        item = MenuItem.objects.get(title="Ice Cream")
        # The assertEqual() method is used to check that two values are equal.
        self.assertEqual(item.price, 80)

    def test_get_all(self):
        # The all() method is used to retrieve all objects from the database.
        items = MenuItem.objects.all()
        # The assertEqual() method is used to check that two values are equal.
        self.assertEqual(len(items), 2)

# Create your tests here.