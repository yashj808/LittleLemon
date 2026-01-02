# This file defines the views for the LittlelemonAPI app.
# A view is a Python function or class that takes a web request and returns a web response.
# The response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really.
# In this case, the views are API endpoints that return JSON data.
from rest_framework import status # Import the status module from Django REST Framework for HTTP status codes
from rest_framework.response import Response # Import the Response class for sending responses
from rest_framework.decorators import api_view, throttle_classes, permission_classes # Import the api_view decorator for creating API views
from .models import MenuItem # Import the MenuItem model from the current directory
from .serializers import MenuItemSerializer # Import the MenuItemSerializer from the current directory
from .models import Category # Import the Category model from the current directory
from .serializers import CategorySerializer # Import the CategorySerializer from the current directory
from django.core.paginator import Paginator, EmptyPage
from rest_framework.response import Response 
from rest_framework import viewsets 
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .throttles import TenCallsPerMinute

from rest_framework.permissions import IsAuthenticated

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_class = ['price', 'inventory']
    search_fields = ['title', 'category__title']

@api_view(['GET', 'POST']) # A decorator that specifies the allowed HTTP methods for this view
def menu_items(request): # A view function to handle requests for all menu items
    if request.method == 'GET': # If the request method is GET
        items = MenuItem.objects.select_related('category').all() # Get all MenuItem objects from the database, including their related Category
        
        # Make query parameter keys lowercase for case-insensitive access
        params = {k.lower(): v for k, v in request.query_params.items()}
        category_name = params.get('category')
        to_price = params.get('to_price')
        search = params.get('search')
        ordering = params.get('ordering')
        perpage = int(params.get('perpage', 2)) #Value is typecasted into int to becuase the params does not handle query params
        page = int(params.get('page', 1))

        if category_name:
            items = items.filter(category__title__iexact=category_name) # Use iexact for case-insensitive matching
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serializer = MenuItemSerializer(items, many=True) # Serialize the list of menu items
        return Response(serializer.data) # Return the serialized data as a response

    elif request.method == 'POST': # If the request method is POST
        serializer = MenuItemSerializer(data=request.data) # Create a new serializer with the request data
        if serializer.is_valid(): # If the data is valid
            serializer.save() # Save the new menu item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Return the new menu item with a 201 Created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # If the data is invalid, return a 400 Bad Request status

@api_view(['GET', 'POST']) # A decorator that specifies the allowed HTTP methods for this view
def single_menu_item(request, pk): # A view function to handle requests for a single menu item
    try: # Try to get the menu item with the specified primary key
        item = MenuItem.objects.get(pk=pk) # Get the MenuItem object with the specified primary key
    except MenuItem.DoesNotExist: # If the menu item does not exist
        return Response(status=404) # Return a 404 Not Found status
    serialized_item = MenuItemSerializer(item) # Serialize the menu item
    return Response(serialized_item.data) # Return the serialized data as a response

@api_view(['GET', 'POST']) # A decorator that specifies the allowed HTTP methods for this view
def categories(request): # A view function to handle requests for all categories
    if request.method == 'GET': # If the request method is GET
        categories = Category.objects.all() # Get all Category objects from the database
        serializer = CategorySerializer(categories, many=True) # Serialize the list of categories
        return Response(serializer.data) # Return the serialized data as a response

    elif request.method == 'POST': # If the request method is POST
        serializer = CategorySerializer(data=request.data) # Create a new serializer with the request data
        if serializer.is_valid(): # If the data is valid
            serializer.save() # Save the new category to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Return the new category with a 201 Created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # If the data is invalid, return a 400 Bad Request status
    
@api_view(['GET', 'PUT', 'DELETE']) # A decorator that specifies the allowed HTTP methods for this view
def single_category(request, pk): # A view function to handle requests for a single category
    try: # Try to get the category with the specified primary key
        category = Category.objects.get(pk=pk) # Get the Category object with the specified primary key
    except Category.DoesNotExist: # If the category does not exist
        return Response(status=status.HTTP_404_NOT_FOUND) # Return a 404 Not Found status

    if request.method == 'GET': # If the request method is GET
        serializer = CategorySerializer(category) # Serialize the category
        return Response(serializer.data) # Return the serialized data as a response

    elif request.method == 'PUT': # If the request method is PUT
        serializer = CategorySerializer(category, data=request.data) # Create a new serializer with the request data
        if serializer.is_valid(): # If the data is valid
            serializer.save() # Save the updated category to the database
            return Response(serializer.data) # Return the updated category
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # If the data is invalid, return a 400 Bad Request status

    elif request.method == 'DELETE': # If the request method is DELETE
        category.delete() # Delete the category from the database
        return Response(status=status.HTTP_204_NO_CONTENT) # Return a 204 No Content status
    
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"messgae":"Some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message": "Only manager should see this"})
    else:
        return Response({'message': "You are not authorized"}, 403)
    
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"message for the logged in users only"})