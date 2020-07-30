from django.db import models

# Create your models here.
class UserAdd(models.Model):
    email  = models.EmailField(unique=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=30,null=True)
    pic = models.ImageField(upload_to="static/images") #upload the images given by user in this path
    def __str__(self):
        return f"{self.email}"    

#create table tablename(attr_name data_type(range))