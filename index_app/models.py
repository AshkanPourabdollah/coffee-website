from django.db import models

# Create your models here.


# coffee list
class Coffee(models.Model):
    coffeeName=models.CharField(default='',max_length=50)
    coffeeImage=models.ImageField(upload_to="images")
    coffeeSmall=models.IntegerField(default=20)
    coffeeBig=models.IntegerField(default=20)

    def __str__(self):
        return self.coffeeName
    
# client comments
class ClientComment(models.Model):
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=60,default='')
    text=models.TextField(max_length=1000,default='')

    def __str__(self):
        return self.name
