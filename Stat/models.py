from django.db import models

# Create your models here.
class AdminDetail(models.Model):
    name=models.CharField(max_length=20,db_column='Name')
    password=models.CharField(max_length=10)
    dept=models.CharField(max_length=5,null=True)
#student table
class ThirdCSE(models.Model):
    roll =models.CharField(max_length=10);
    name=models.CharField(max_length=30);
    CompilerDesign=models.CharField(max_length=120)
    MachineLearning=models.CharField(max_length=120)
    InternetOfThing=models.CharField(max_length=120)
    IPR=models.CharField(max_length=120)
    SoftwareTesting=models.CharField(max_length=120)
class OE(models.Model):
    roll=models.CharField(max_length=10)
    oesubject=models.CharField(max_length=20)
    oeat=models.CharField(max_length=120)
    branch=models.CharField(max_length=10,null=True)
    
    



