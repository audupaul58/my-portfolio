from django.db import models

# Create your models here.


class Skills(models.Model):
    title = models.CharField(max_length=255)
    level = models.IntegerField(default=0)
    color = models.CharField(max_length=255, default='blue')
    
    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    url = models.URLField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('added_on',)


