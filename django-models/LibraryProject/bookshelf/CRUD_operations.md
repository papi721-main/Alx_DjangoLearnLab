```python
# Create
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b.save()
b   # Output: <Book: Book object (1)>
# Retrieve
book = Book.objects.get(title="1984")
book.title                  # Output: '1984'
book.author                 # Output: 'George Orwell'
book.publication_year   # Output: 1949
# Update
book.title = "Nineteen Eighty-Four"
book.save()
book = Book.objects.get(title="Nineteen Eighty-Four")
book.title    # Output: 'Nineteen Eighty-Four'
# Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```
