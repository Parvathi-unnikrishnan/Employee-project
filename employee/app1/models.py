from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    address=models.TextField()
    age=models.IntegerField()
    email=models.CharField(max_length=20)
    image=models.ImageField(upload_to="img",blank=True,null=True)

    def __str__(self):
        return self.name