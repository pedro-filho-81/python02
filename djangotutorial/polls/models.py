from django.db import models

# Create your models here.

# Define the Question and Choice models for the polls application

# Each model is a Python class that subclasses django.db.models.Model

# The models define the structure of the database tables    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)