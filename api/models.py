from django.db import models

import uuid

# Create your models here.

class assigment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    descritpion = models.CharField(max_length=200)
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    













# class Paid(models.Model):
#      user=models.ForeignKey(User)
#      eyw_transactionref=models.CharField(max_length=100, null=True, blank=True, unique=True)

#      def __init__(self):
#          super(Paid, self).__init__()
#          self.eyw_transactionref = str(uuid.uuid4())

#      def __unicode__(self):
#          return self.user