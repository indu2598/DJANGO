from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    authorname = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)

    def __str__(self):
        return self.id
    
    
    