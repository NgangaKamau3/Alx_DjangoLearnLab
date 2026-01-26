### Update a Book instance
```python
from bookshelf.models import Book
book = Book.objects.update(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984 by George Orwell (1949)
```