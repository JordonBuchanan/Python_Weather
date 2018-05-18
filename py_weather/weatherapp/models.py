from django.db import models

#Weather database model for sqlite
class City(models.Model):
    name = models.CharField(max_length=20)
    #Name of city
    def __str__(self):
        return self.name
    #changes 'citys' to actual plural
    class Meta:
        verbose_name_plural = 'cities'