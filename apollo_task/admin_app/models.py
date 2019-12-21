from django.db import models

class EmployeeModel(models.Model):
    empID=models.IntegerField(primary_key=True)
    empName=models.CharField(max_length=30)
    contactNo=models.IntegerField(unique=True,default=False)
    emailID=models.EmailField(unique=True)
    designation=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    status = models.CharField(max_length=30,default=False)

    def __str__(self):
        return '{}'.format(self.empID)


class TaskAssigning(models.Model):
    taskno=models.AutoField(primary_key=True)
    taskname=models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    empID=models.ForeignKey(EmployeeModel,on_delete=models.CASCADE)
