from django.db import models

class Member(models.Model):
    chairman = models.CharField(max_length=250, null=True, blank=True, default="")
    kagawad1 = models.CharField(max_length=250, null=True, blank=True)
    kagawad2 = models.CharField(max_length=250, null=True, blank=True)
    kagawad3 = models.CharField(max_length=250, null=True, blank=True)
    kagawad4 = models.CharField(max_length=250, null=True, blank=True)
    kagawad5 = models.CharField(max_length=250, null=True, blank=True)
    kagawad6 = models.CharField(max_length=250, null=True, blank=True)
    kagawad7 = models.CharField(max_length=250, null=True, blank=True)
    treasurer = models.CharField(max_length=250, null=True, blank=True)
    secretary = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.chairman
    
