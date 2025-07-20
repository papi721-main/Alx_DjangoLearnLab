#!/usr/bin/env python3
"""Setup sample data for the relationship_app in LibraryProject.

To run this script, use the command:
    python -m relationship_app.setup_sample_data
"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Librarian, Library

confirm = (
    input("Do you want to delete all data in the models? (yes/no): ").strip().lower()
)
if confirm == "yes":
    Author.objects.all().delete()
    Book.objects.all().delete()
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    print("All data deleted.")


# Create Authors
author1 = Author.objects.create(name="Pope Shenouda III")
author2 = Author.objects.create(name="George Orwell")

# Create Libraries
library1 = Library.objects.create(name="Coptic Library")
library2 = Library.objects.create(name="Central Library")

# Create Books
book1 = Book.objects.create(title="The Release of the Spirit", author=author1)
book2 = Book.objects.create(title="1984", author=author2)
book3 = Book.objects.create(title="Nineteen Eighty-Four", author=author2)

# Add books to libraries
library1.books.add(book1)
library2.books.add(book2, book3)

# Create Librarians
librarian1 = Librarian.objects.create(name="Sarah Johnson", library=library1)
librarian2 = Librarian.objects.create(name="John Smith", library=library2)
print("Sample data created successfully.")
