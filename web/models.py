from django.db import models

# Create your models here.
class Project(models.Model):
    image=models.ImageField(upload_to='media/Project')
    heading=models.CharField(max_length=500)
    title=models.CharField(max_length=500)
    year=models.IntegerField()
    description=models.CharField(max_length=500)
    business=models.CharField(max_length=500)
    technic=models.CharField(max_length=500)

    def __str__(self):
       return self.heading
    


