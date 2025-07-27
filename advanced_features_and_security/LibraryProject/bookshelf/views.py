from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.utils.html import escape

# Create a new book (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = escape(request.POST.get('title', '').strip())
        author = escape(request.POST.get('author', '').strip())
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book_list')

    return render(request, 'bookshelf/create_book.html')


# Edit an existing book (requires can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = escape(request.POST.get('title', '').strip())
        book.author = escape(request.POST.get('author', '').strip())
        book.published_date = request.POST.get('published_date')

        if book.title and book.author and book.published_date:
            book.save()
            return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# List all books (requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})
