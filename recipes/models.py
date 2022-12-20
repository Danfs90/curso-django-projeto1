from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    process_time = models.IntegerField()
    process_time_unit = models.CharField(max_length=65)
    difficulty = models.IntegerField()
    difficulty_unit = models.IntegerField()
    process = models.TextField()
    process_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
