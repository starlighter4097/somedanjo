from django.db import models 

# Create your models here.

class attendance(models.Model):
    Roll_no = models.PositiveIntegerField(default='')
    Student_Name = models.CharField(max_length=20,default='')
    Period1 = models.CharField(max_length=10,default='')
    Period2 = models.CharField(max_length=10,default='')
    Period3 = models.CharField(max_length=10,default='')
    Period4 = models.CharField(max_length=10,default='')
    Period5 = models.CharField(max_length=10,default='')
    Period6 = models.CharField(max_length=10,default='')
    Period7 = models.CharField(max_length=10,default='')






