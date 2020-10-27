from django.db import models
from django import forms
import datetime

# Create your models here.

class Question(models.Model):
	type = models.CharField(max_length=15, default="", null=True, blank=True)
	action = models.CharField(max_length=300)
	length = models.IntegerField(default=0)
	choices = models.CharField(max_length=500, default="", null=True, blank=True)
	is_fork = models.BooleanField(default=False)
	date_published = models.DateTimeField('date published', auto_now_add=True)
	addedby = models.CharField(max_length=100, default="Anymous")

class QuestionFlow(models.Model):
	parent = models.ForeignKey(Question, on_delete=models.CASCADE)
	son = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.CharField(max_length=100, default="", null=True, blank=True)

class User(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=100)

class Interview(models.Model):
	date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Answer(models.Model):
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=500, null=True)
	choice_vid = models.FileField(upload_to='videos/', null=True,)

class VideoModel(models.Model):
	video = models.FileField(upload_to='videos/')
	# answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

