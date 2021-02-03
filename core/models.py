from django.db import models

# Masters
from authentification.models import User


class Tag(models.Model):
    label = models.CharField(max_length=255)


class New(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='new_sender', null=True)
    url = models.URLField()
    topic = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)


class NewData(models.Model):
    views_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='message_sender', null=True)
    content = models.TextField()
    parent_new = models.ForeignKey(New, null=True, on_delete=models.SET_NULL)
    parent_message = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)


class MessageData(models.Model):
    message = models.OneToOneField(Message, related_name='data', on_delete=models.SET_NULL, null=True)
    sender = models.OneToOneField(User, related_name='user_valoration', on_delete=models.SET_NULL, null=True)
    agree = models.BooleanField(default=False)
    disagree = models.BooleanField(default=False)
    offtopic = models.BooleanField(default=False)
    context_value = models.FloatField(default=0.00)


class Notification(models.Model):
    service_name = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.service_name
