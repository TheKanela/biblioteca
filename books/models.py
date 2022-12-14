from django.db import models
from uuid import uuid4

# Create your models here.
class Books(models.Model):
    bookID= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=255)
    releaseYear= models.IntegerField()
    state = models.CharField(max_length=50)
    pages= models.IntegerField()
    publishingCompany= models.CharField(max_length=255)
    createAt= models.DateTimeField(auto_now_add=True)