from django.db import models

# Create your models here.


# #必须继承models。Model模块
class Person(models.Model):

    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Press(models.Model):
    #出版社应该应该有id 和出版社
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=30)

class book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    press = models.ForeignKey(to='Press')
