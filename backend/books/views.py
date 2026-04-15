from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# GET all books
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# GET single book
@api_view(['GET'])
def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)

    serializer = BookSerializer(book)
    return Response(serializer.data)


# POST new book
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

from rest_framework.decorators import api_view
from rest_framework.response import Response

import sys
import os

# path fix for ai_engine
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "..", "ai_engine"))

from rag_pipeline import rag_pipeline


@api_view(['GET'])
def search_books(request):
    query = request.GET.get('q')

    if not query:
        return Response({"error": "Query missing"})

    results = rag_pipeline(query)

    return Response({
        "query": query,
        "results": results
    })