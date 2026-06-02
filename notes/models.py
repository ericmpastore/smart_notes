from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    count_likes = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    is_public = models.BooleanField(default=False)