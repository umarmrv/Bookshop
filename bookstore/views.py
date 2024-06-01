from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    books = models.Books.objects.all()
    return HttpResponse(''.join([str(book) + '<br>' for book in books]))
