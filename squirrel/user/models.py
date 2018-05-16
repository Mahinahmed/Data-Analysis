from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Client(User):
    full_name = models.CharField(
        max_length=50, verbose_name='Full Name :')

    # zip_code = models.IntegerField(
    #     default=0000, verbose_name='ZIP Code :')
    #
    # dateOfBirth = models.DateField(
    #     verbose_name='Date-of-birth : '
    # )

    def __str__(self):
        return '{name}'.format(name=self.full_name)
