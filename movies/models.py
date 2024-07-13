from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=30, null=False)
    director = models.CharField(max_length=45, null=False)
    publication= models.CharField(max_length=30)
    synopsis = models.TextField(max_length=800, null=False)
    
    def __str__(self) -> str:
        return self.name
