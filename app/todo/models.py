from django.db import models
from django.conf import settings
# Create your models here.

class OwnedModel(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

class Todo(OwnedModel, models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#class User(model.Model):
#    username = models.CharField(max_length=100)
#    password = models.CharField(max_length=100)

    