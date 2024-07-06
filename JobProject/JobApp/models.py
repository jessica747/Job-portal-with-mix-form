from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomeUser_model(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker'),
    ]
    User_Type=models.CharField(choices=USER,max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    GENDER=[
        ('male','Male'),
        ('female','Female'),            
        ('other','Other'),              
    ]
    Gender=models.CharField(choices= GENDER,max_length=100,null=True)
    Profile_Picture=models.ImageField(upload_to='media/profilepicture',null=True)

class BasicInformation_model(models.Model):
    portaluser=models.OneToOneField(CustomeUser_model,on_delete=models.CASCADE,related_name='basicinfomodel',null=True)
    Faters_Name=models.CharField(max_length=100,null=True)
    Mothers_Name=models.CharField(max_length=100,null=True)
    MARITALSTATUS=[
        ('married','Married'),
        ('unmarried','Unmarried'),
    ]
    Marital_Status=models.CharField(choices=MARITALSTATUS,max_length=100,null=True)
    Date_Of_Birth=models.DateField(null=True)

class ContactInformation_model(models.Model):
    portaluser=models.OneToOneField(CustomeUser_model,on_delete=models.CASCADE,related_name='contactinfomodel',null=True)
    Mobil_Number=models.CharField(max_length=100,null=True)
    Emergency_Contact=models.CharField(max_length=100,null=True)
    Present_Address=models.CharField(max_length=100,null=True)
    Permanent_Address=models.CharField(max_length=100,null=True)


class EducationQualifiction(models.Model):
    seekeruser=models.ForeignKey(CustomeUser_model,on_delete=models.CASCADE,related_name='eduinfomodel',null=True)
    Degree=models.CharField(max_length=100,null=True)
    Passing_Year=models.CharField(max_length=100,null=True)
    Grade=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)

class WorkExperiance(models.Model):
    seekeruser=models.ForeignKey(CustomeUser_model,on_delete=models.CASCADE,related_name='workexinfomodel',null=True)
    Company_Name=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    Duration=models.CharField(max_length=100,null=True)
    Department=models.CharField(max_length=100,null=True)


class AddJob_Model(models.Model):
    recruiteruser=models.ForeignKey(CustomeUser_model,on_delete=models.CASCADE,related_name='addinfomodel',null=True)
    Job_Title=models.CharField(max_length=100,null=True)
    Company_Name=models.CharField(max_length=100,null=True)
    Company_Description=models.TextField(null=True)
    Company_Logo=models.ImageField(upload_to='media/logo',null=True)
    Company_Location=models.CharField(max_length=200,null=True)
    Qualifications=models.CharField(max_length=100,null=True)
    Dead_Line=models.DateField(null=True)
    Salary=models.CharField(max_length=100,null=True)


class Applyjob_Model(models.Model):
    Applicant=models.ForeignKey(CustomeUser_model,on_delete=models.CASCADE,related_name='applyjob',null=True)
    Applied_job=models.ForeignKey(AddJob_Model,on_delete=models.CASCADE,null=True)
    Skills=models.CharField(max_length=100,null=True)
    Resume=models.FileField(upload_to='media/resume',null=True)
    Seeker_Profile_Pic=models.ImageField(upload_to='media/image',null=True)
    Status=models.CharField(default='Pending',max_length=200,null=True)
