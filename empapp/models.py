from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    #address = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    salary=models.IntegerField()

    class Meta:
        db_table="Emp_Info"

class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    emp = models.OneToOneField(Employee,on_delete=models.CASCADE)
    class Meta:
        db_table="Address_Info"