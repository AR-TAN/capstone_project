from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Adopt(models.Model):
    name = models.CharField(max_length=40)
    breed = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    years_old = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return "{} - {}".format(self.name, self.breed)
        
g