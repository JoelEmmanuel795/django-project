from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text='Enter the exact time!')

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.time_log)