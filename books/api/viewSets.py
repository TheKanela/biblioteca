from rest_framework import viewsets

from books.api import serializers
from books import models

class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
    http_method_names= ['get', "post", 'put', 'patch', 'options', 'delete']