from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quote(models.Model):
    content = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text