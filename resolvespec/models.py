from django.db import models

# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ManyToManyField("self", symmetrical=False, related_name="children")
    oneormany = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    
