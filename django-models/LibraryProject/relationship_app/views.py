#!/usr/bin/env python3
from django.shortcuts import render
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show details for a specific library
class LibraryDetailView(DetailView):
    from .models import Library
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
