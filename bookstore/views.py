from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    books = models.Books.objects.all()

    return render(request, "books.html", {'books': books})
   # return HttpResponse(''.join([str(book) + '<br>' for book in books]))


def single_book(request, book_id):
    books = models.Books.objects.get(pk=book_id)
    return render(request, "single_book.html", {"books": books})
