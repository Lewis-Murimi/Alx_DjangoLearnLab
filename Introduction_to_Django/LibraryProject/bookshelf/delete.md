# Delete the book
```python
from bookshelf.models import Book
books = Book.objects.get()
books.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>
