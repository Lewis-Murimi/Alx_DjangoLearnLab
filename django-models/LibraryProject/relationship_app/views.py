from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Librarian
from django.views.generic import ListView, DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'pk'
