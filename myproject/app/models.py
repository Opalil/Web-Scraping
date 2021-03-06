from django.db import models
from django.utils import timezone
# Create your models here.


class Job(models.Model):
    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table: 'job'
        

    class Admin:
        pass
