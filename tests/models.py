from django.db import models

# Create your models here.


class Employee(models.Model):
    Emp_id = models.IntegerField()
    Name = models.CharField(max_length=200, null=True)
    Mobile = models.BigIntegerField()

    def __str__(self):
        return self.Name


class Department(models.Model):
    depart_id = models.IntegerField()
    depart_name = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.depart_id


class Coursenotes(models.Model):
    course_dtl = models.CharField(max_length=200)
    coursename = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_dtl
