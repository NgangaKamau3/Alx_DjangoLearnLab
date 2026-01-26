### Update a Book instance
```python
from bookshelf.models import Book
book = Book.objects.update("book.title", "Nineteen Eighty-Four")
print(book)
# Output: 1984 by George Orwell (1949)
```