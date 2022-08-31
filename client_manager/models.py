from django.db import models

# Create your models here.


class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    date_of_contact = models.DateField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
