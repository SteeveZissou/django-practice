from django.shortcuts import HttpResponse, get_object_or_404, render
from store.models import Book

def books(request):
    books_titles = [book.title for book in Book.objects.all()]
    return render(request,"store/index.html", context={"books_titles":books_titles})

def book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    return render(request, "store/book.html", context={"book":book})
