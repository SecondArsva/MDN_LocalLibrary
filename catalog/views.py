from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre

# Create your views here.

def index(request):
    """View function for home page on site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.all().filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #Challenge
    num_genres = Genre.objects.count()
    q = request.GET.get("q", "").strip()
    num_book_match = 0
    num_book_match = Book.objects.all().filter(title__icontains=q).count() if q else 0

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_genres':num_genres,
        'num_book_match':num_book_match,
        'q':q,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
