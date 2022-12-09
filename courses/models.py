from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    test_form = models.TextField()
    completed = models.BooleanField(default=False)
