from django.db import models

class Books(models.Model):
 bookid = models.IntegerField(primary_key=True)
 title = models.CharField(max_length=50)
 author = models.CharField(max_length=30)
 price = models.FloatField(default=0)
 discount = models.FloatField(default=0)
 qoh = models.IntegerField(default=0)
 description = models.TextField(max_length=300)
