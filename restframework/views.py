from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restframework.models import Book

from restframework.serializers import BookSerializer

# Create your views here.
@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

