from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ("live", "live"),
    ("draft", "draft"),
)

class Photo(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='./assets')
    caption = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='live')
    
