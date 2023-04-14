from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name