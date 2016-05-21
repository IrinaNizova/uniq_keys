from django.db import models

class Key(models.Model):
    STATUSES = (('I', 'issued'), ('R', 'repaid'))
    value = models.CharField(max_length=4, primary_key=True)
    status = models.CharField(max_length=1,choices=STATUSES, default='I')
