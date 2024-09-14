from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    details = models.TextField()
    completed = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
