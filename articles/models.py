from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail 
    # add in author later


    def __str__(self):
        return self.title
