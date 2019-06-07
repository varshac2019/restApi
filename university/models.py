from django.db import models

# Create your models here.


class University(models.Model):
    rank           = models.CharField(max_length=15)
    name            = models.CharField(max_length=150)
    city            = models.CharField(max_length=150)
    location        = models.CharField(max_length=150)
    link_to_program = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class ProgramHighlight(models.Model):
    start_month     = models.CharField(max_length=20,null=True,blank=True)
    class_size      = models.CharField(max_length=10,null=True,blank=True)
    avg_work_experience    = models.CharField(max_length=10,null=True,blank=True)
    avg_student_age    = models.CharField(max_length=10,null=True,blank=True)
    intl_students       = models.CharField(max_length=10,null=True,blank=True)
    women_students      = models.CharField(max_length=10,null=True,blank=True)
    avg_salary     = models.CharField(max_length=30,null=True,blank=True)
    scholarship     = models.CharField(max_length=10,null=True,blank=True)
    accreditations  = models.CharField(max_length=35,null=True,blank=True)
    employed        = models.CharField(max_length=20,null=True,blank=True)
    name            = models.OneToOneField(University,on_delete=models.CASCADE)
#    name            = models.ForeignKey(University,on_delete=models.CASCADE)
#    link_to_program = models.ForeignKey(University,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
