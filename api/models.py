from tastypie.resources import ModelResource
from bookstore.models import Category, Books
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization


class CategoryResourse(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class BookResourse (ModelResource):
    class Meta:
        queryset = Books.objects.all()
        resourse_name = 'books'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()
