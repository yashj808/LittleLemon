# This file defines the views for the LittlelemonAPI app.
# A view is a Python function or class that takes a web request and returns a web response.
# The response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really.
# In this case, the views are API endpoints that return JSON data.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

@api_view(['GET'])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view(['GET'])
def single_menu_item(request, pk):
    try:
        item = MenuItem.objects.get(pk=pk)
    except MenuItem.DoesNotExist:
        return Response(status=404)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)