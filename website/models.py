from django.db import models

class Program(models.Model):
	icon = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	desc = models.TextField() 


class Video(models.Model):
	video_name = models.CharField(max_length=100)
	title = models.CharField(max_length=400)
	video_desc =  models.TextField() 


class Speakers(models.Model): 
	image = models.FileField(upload_to='images') 
	