from django.db import models
from django.utils import timezone
import time
import os
import random

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Rank(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    score = models.IntegerField()
    username = models.CharField(max_length=100, default='...')


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
    def user_dirpath(self, name):
        now = time.strftime('%Y%m%d%H%M%S')
        exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), name)
        while os.path.exists('Files/{0}/{1}'.format(self.user_id, exact_name)):
            exact_name = '{0}_{1}__{2}'.format(now, random.randint(0, 1000), name)
        _path = 'Files/{0}/{1}'.format(self.user_id, exact_name)
        self.path = 'Files/'+_path
        self.origin_name = name
        self.exact_name = exact_name
        return './' + _path

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=user_dirpath)
    user_id = models.IntegerField()
    path = models.CharField(max_length=500, default='')
    origin_name = models.CharField(max_length=255, default=name)
    exact_name = models.CharField(max_length=255, default=origin_name)
