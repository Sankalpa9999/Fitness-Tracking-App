from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='static/image/',null=True,blank=True)
    email = models.EmailField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name