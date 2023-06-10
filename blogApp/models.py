from django.db import models
from django.contrib.auth.models import User
from django_editorjs_fields import EditorJsTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = EditorJsTextField()
    image = models.ImageField(upload_to='postImages/')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=360)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name.upper()}"