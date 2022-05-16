from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.question
