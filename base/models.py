from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import User

class CustomUser(User):
    is_filled = models.BooleanField(default=False)
    mark = models.IntegerField(default=0)
    evaluation = models.CharField(max_length=500, default='')

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Room(BaseModel):
    FormName = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    def __str__(self):
        return self.FormName
    
class Question(BaseModel):
    room =  models.ForeignKey(Room, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=200)
    marks = models.IntegerField(default=0)


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answer')
    option = models.CharField(max_length=100)
    mark = models.IntegerField(default=0)
    note = models.CharField(max_length=5000, default='')


class HomeQuestions(models.Model):
    id = models.CharField(primary_key=True, editable=True, max_length=3)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


