from django.db import models

## create functional user interface with 
## to register/Login users with fields [username]


class Register(models.Model):
    HIV_STATUS = (
        ('positive', 'positive'),
        ('negative', 'negative'),
        ('unknown', 'unknown'),
    )
    username = models.CharField(max_length=100,blank=True,null=True)
    age  = models.IntegerField(blank=True,null=True)
    FirstName = models.CharField(max_length=100,blank=True,null=True)
    SurName = models.CharField(max_length=100,blank=True,null=True)
    Hiv_status = models.CharField(max_length=100,choices=HIV_STATUS,blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.username


class Login(models.Model):
    username = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)



