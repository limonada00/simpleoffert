from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

class SimpleOfert(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image_field = models.ImageField()
    author = models.ForeignKey(User, related_name='authors')
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Categories, related_name='categorys')

    def __str__(self):
        return self.title