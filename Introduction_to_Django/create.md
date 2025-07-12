```python
from bookshelf.models import Book
b = Book(title="1984", author="George Orwell", publication_year=1949)
b.save()
b   # Output: <Book: Book object (1)>
```
