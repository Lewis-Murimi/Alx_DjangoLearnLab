from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    Fields:
    - name: The full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Fields:
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey linking to the Author model (many books can belong to one author).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
