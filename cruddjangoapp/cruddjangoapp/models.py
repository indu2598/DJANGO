from django.db import models

class Task(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 150)
    authorname = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)
    
    # class Meta:
    #     db_table = "cruddjangoapp_task"

    def __str__(self):
        return self.name


