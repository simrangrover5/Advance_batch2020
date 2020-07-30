from django.db import models
from user.models import UserAdd
from datetime import datetime
# Create your models here.
class Addblog(models.Model):
    author = models.ForeignKey(to=UserAdd,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=2000)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.author}"

