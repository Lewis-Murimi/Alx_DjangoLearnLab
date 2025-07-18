from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Library, Book, Librarian
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    def get_form(self, form_class=None):
        return UserCreationForm()

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

def is_admin(user):
    return hasattr(user,'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user,'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user,'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/librarian_view.html', {'libraries': libraries})

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')