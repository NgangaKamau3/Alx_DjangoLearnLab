### Deleting a Book instance
```python
from bookshelf.models import Book
book = Book.objects.delete("book.delete")
print(book)
# Output: 1984 by George Orwell (1949)
```