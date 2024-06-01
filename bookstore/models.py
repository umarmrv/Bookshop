from django.db import models
from django.utils import timezone


class Category(models.Model):
    # CharFaild титле будет ввиде строки
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  # это функция магический метод который отображает имя категории


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # foreinKey  это типа принимаем ключ  из другой таблици
    # on_delete=models.CASCADE это значил при удаление категории и книгам тоже конец
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
