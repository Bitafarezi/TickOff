from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    task = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=100)
    desc = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title