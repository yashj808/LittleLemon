from rest_framework import serializers # Import the serializers module from Django REST Framework
from .models import MenuItem # Import the MenuItem model from the current directory
from .models import Category # Import the Category model from the current directory
from decimal import Decimal # Import the Decimal module for precise decimal arithmetic
import bleach

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

class CategorySerializer(serializers.ModelSerializer): # Define a serializer for the Category model
    class Meta: # The Meta class specifies metadata for the serializer
        #Not added yet (Relationship Serializer)
        model = Category # The model to be serialized
        fields = ['id', 'slug', 'title'] # The fields to be included in the serialized output
    
    def validate_title(self, value):
        return bleach.clean(value, tags=[], attributes={}, strip=True)

class MenuItemSerializer(serializers.ModelSerializer): # Define a serializer for the MenuItem model
    stock = serializers.IntegerField(source='inventory') # Map the 'stock' field to the 'inventory' model field
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax') # A custom field that gets its value from a method
    category = CategorySerializer(read_only=True) # A nested serializer for the 'category' field (read-only)
    category_id = serializers.IntegerField(write_only=True) # A field for the category ID (write-only)
    class Meta: # The Meta class specifies metadata for the serializer
        model = MenuItem # The model to be serialized
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id'] # The fields to be included in the serialized output

    def validate_title(self, value):
        return bleach.clean(value, tags=[], attributes={}, strip=True)

    def calculate_tax(self, product:MenuItem) -> Decimal: # A method to calculate the price after tax
        return product.price * Decimal(1.1) # Calculate and return the price with a 10% tax
    
    def create(self, validated_data): # A method to handle the creation of a new MenuItem
        category_data = validated_data.pop('category', None) # Get the category data from the validated data

        if category_data: # If category data is present
            category, _ = Category.objects.get_or_create( # Get or create a Category object
                slug=category_data['slug'], # The slug of the category
                defaults={'title': category_data['title']} # The title of the category
            )
            validated_data['category'] = category # Set the category of the MenuItem

        return super().create(validated_data) # Call the parent's create method to create the MenuItem