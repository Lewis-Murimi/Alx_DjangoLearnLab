# Delete the book
```python
from bookshelf.models import Book
book = Book.objects.get()
book.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>
