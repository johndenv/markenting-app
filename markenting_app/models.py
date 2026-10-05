from django.db import models

class DataMovie(models.Model):  
    text = models.TextField()
    context = models.CharField(max_length=400)
    public = models.CharField(max_length=100)
    number_public = models.IntegerField() 

    def __str__(self):
        return self.context
