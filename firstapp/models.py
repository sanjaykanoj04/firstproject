from django.db import models
from django.db import models

class TutorReg(models.Model):
    password=models.CharField(max_length=10)
    mobileno=models.CharField(max_length=10)
    fname=models.CharField(max_length=10)

    def __str__(self):
        return "Password is"+str(self.password)+"mobileno is"+str(self.mobileno)+"fname is"+str(self.fname)
    