from django.db import models


# Create your models here.
class BooksModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
