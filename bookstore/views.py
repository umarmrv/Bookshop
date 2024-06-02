from django.shortcuts import render
from django.http import Http404
from . import models


def index(request):
    books = models.Books.objects.all()

    return render(request, "books.html", {'books': books})
   # return HttpResponse(''.join([str(book) + '<br>' for book in books]))


def single_book(request, book_id):
    try:
        books = models.Books.objects.get(pk=book_id)
        return render(request, "single_book.html", {"books": books})
    except models.Books.DoesNotExist:
        raise Http404()


def book_detail(request, book_id):
    book = models.Books.objects.get(pk=book_id)
    return render(request, 'single_book.html', {'book': book})
