from django.db import models

# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ManyToManyField("self", related_name="children", blank=True, null=True)
    oneormany = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Content(models.Model):
    node = models.ForeignKey(Node)
    description = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.node.name

    
