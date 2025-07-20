#!/usr/bin/env python3
"""Query samples for the relationship_app in LibraryProject.

This is a standalone script to demonstrate querying the models
defined in the relationship_app.

In order to run this script, use the command:
    python -m relationship_app.query_samples
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Librarian, Library

# Query all books by a specific author
author_name = "Pope Shenouda III"
author = Author.objects.get(name=author_name)
b = Book.objects.filter(author=author)
print(b)

# List all books in a library
library_name = "Coptic Library"
l = Library.objects.get(name=library_name)
print(l.books.all())

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=l)
print(librarian)