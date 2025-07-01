from django.db import models

from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    age = models.IntegerField()
    arrival_date = models.DateField()
    adopted = models.BooleanField(default=False)
    
    def str(self):
        return self.name
