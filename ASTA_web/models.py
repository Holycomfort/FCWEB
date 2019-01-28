from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user_id = models.IntegerField()


class UploadFile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='Files')
    user_id = models.IntegerField()
