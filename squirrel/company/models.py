from django.db import models

from user.models import User
from .constants import COMPANY_TYPES, IntegerRangeField


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Company Name :')
    type = models.CharField(max_length=50, verbose_name='Company Type :',
                            choices=COMPANY_TYPES)
    address = models.CharField(max_length=300, verbose_name='Company Address :')
    email = models.EmailField(verbose_name='Company contact E-mail :')
    phone = models.CharField(default='+880', verbose_name='Phone Number :', max_length=15)
    overview = models.CharField(max_length=500, verbose_name='Overview :')
    established = models.DateField(verbose_name='Established on :')
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return '{company_name}'.format(company_name=self.name)

    def filtered_set(self,type):
        return Company.objects.all.filter(type=type)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rating = IntegerRangeField(max_value=5, min_value=1)
    comment = models.CharField(max_length=300, verbose_name='Comment :')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{user} on {company}'.format(user=self.user, company=self.company)

# class ScrapeCompany(models.Model):
#     name = models.CharField(max_length= 200, verbose_name='Company Name')
#     position = models.CharField(max_length= 200, verbose_name='Position')
#
#     def __str__(self):
#         return '{company_name}'.format(company_name=self.name)
