from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# each class = 1 model in the DB
class Post(models.Model):
    title = models.CharField(max_length=64)
    # unrestricted block of text
    content = models.TextField()
    # auto_now = True - but every POST makes it update the date
    # auto_now_add=True - this creates date upon creation but you cannot change it afterwards
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title