from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#class User(model.Model):
#    username = models.CharField(max_length=100)
#    password = models.CharField(max_length=100)

    