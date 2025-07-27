from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Create logic here
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Edit logic here
    return render(request, 'edit_book.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})
