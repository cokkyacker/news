from django.db import models

# Create your models here.
from login.models import Users


class ArticleType(models.Model):
    title = models.CharField(max_length=256, unique=True)

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=10240)

    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
