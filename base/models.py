from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants',blank=True)
    update = models.DateTimeField(auto_now=True)            #auto_now take snapshot everytime there is updation in room
    create = models.DateTimeField(auto_now_add=True)        #auto_now_add take snapshot when it is created for first time
    
    class Meta:
        ordering = ['-update','-create']


    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)     #if room get deleted all the message would be deleted 
    body = models.TextField()

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-create']

    def __str__(self):
        return self.body[0:50]
