from django.db import models

# Create your models here.
class Size(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Pizza(models.Model):
    topping1=models.CharField(max_length=100)
    topping2=models.CharField(max_length=100)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    


# now we can use these models to create forms even in better way than just making forms 