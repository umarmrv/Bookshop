from django.urls import path
from . import views

app_name = 'bookstore'
urlpatterns = [
    path('', views.index, name="index"),
    path('book/<int:book_id>', views.single_book, name='single_book')
]
