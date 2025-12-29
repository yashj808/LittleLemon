# This file is used to write tests for the LittlelemonAPI app.
# Tests are used to check that your code is working correctly.
# Django provides a test framework that allows you to write and run tests for your app.

from django.test import TestCase
from .models import MenuItem, Category
from .serializers import MenuItemSerializer

# The TestCase class is a subclass of the standard Python unittest.TestCase class.
# It provides a number of additional assertion methods that are useful for testing web applications.
class MenuItemTest(TestCase):
    # The setUp method is called before each test method is run.
    # It is used to set up any objects that are needed for the tests.
    def setUp(self):
        self.category = Category.objects.create(slug="test-desserts", title="Desserts")
        MenuItem.objects.create(title="Ice Cream", price=80, inventory=100, category=self.category)
        MenuItem.objects.create(title="Cake", price=100, inventory=50, category=self.category)

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
    
    def test_title_html_stripping(self):
        """
        Tests that HTML tags are stripped from the title field during serialization.
        """
        data = {
            "title": "<a>HTML</a> Title",
            "price": "50.00",
            "stock": 30,
            "category_id": self.category.id
        }
        serializer = MenuItemSerializer(data=data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        self.assertEqual(serializer.validated_data['title'], "HTML Title")


# Create your tests here.