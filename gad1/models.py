from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	mobileno = models.CharField(max_length=20)
	year = models.CharField(max_length=20)
	div = models.CharField(max_length=20)
	sap = models.CharField(primary_key=True,max_length=20)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Professor(models.Model):
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=20)
	mobileno = models.CharField(max_length=20)
	department = models.CharField(max_length=20)
	sap = models.CharField(primary_key=True,max_length=20)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class Classes_taught(models.Model):
	sapct = models.ForeignKey(Professor)
	FE_A = models.BooleanField()
	SE_A = models.BooleanField()
	TE_A = models.BooleanField()
	BE_A = models.BooleanField()
	FE_B = models.BooleanField()
	SE_B = models.BooleanField()
	TE_B = models.BooleanField()
	BE_B = models.BooleanField()

class AssgProfessor(models.Model):
	sapap = models.ForeignKey(Professor)
	assgid = models.CharField(primary_key=True,max_length=20)
	date = models.DateField()
	forwarded = models.BooleanField()



class AssgStudent(models.Model):
	sapas = models.ForeignKey(Student)
	assgas = models.ForeignKey(AssgProfessor)
	marks = models.IntegerField(default=999)
	uploaded = models.BooleanField()


