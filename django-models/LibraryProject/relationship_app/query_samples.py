import os
import django
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'relationship_app.settings')
django.setup()
from .models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# Query 2: List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
