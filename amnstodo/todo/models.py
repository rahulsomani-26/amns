from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'