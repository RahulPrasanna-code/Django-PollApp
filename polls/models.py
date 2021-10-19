from django.db import models
from django.db.models.base import Model

class Poll(models.Model):
    pollquestion=models.TextField()
    option1=models.CharField(max_length=65)
    option2=models.CharField(max_length=65)
    option3=models.CharField(max_length=65)
    option1_count=models.IntegerField(default=0)
    option2_count=models.IntegerField(default=0)
    option3_count=models.IntegerField(default=0)

    def total(self):
        return self.option1_count+self.option2_count+self.option3_count
    
    
