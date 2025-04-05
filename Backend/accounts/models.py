from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    staff_status = models.BooleanField(default=False)
    def __str__(self):
        return self.name