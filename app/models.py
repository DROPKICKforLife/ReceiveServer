from django.db import models
class Receive(models.Model):
    rec_text = models.CharField(max_length=200)
    rec_date = models.DateTimeField('date published')

    pass

# Create your models here.
