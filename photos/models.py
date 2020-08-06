from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

STATUS_CHOICES = (
    ("live", "live"),
    ("draft", "draft"),
)

def file_size(value): 
    limit = 300
    limit_kb = limit*1024
    if value.size > limit_kb:
        raise ValidationError('File too large. Size should not exceed {} Kb. Current file size is {} Kb'.format(limit, value.size//1024))

class Photo(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='./assets', validators=[file_size])
    caption = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='live')
    
