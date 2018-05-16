from django.contrib import admin

# Register your models here.
from company.models import Company, Review
    # ScrapeCompany

admin.site.register(Company)
admin.site.register(Review)
# admin.site.register(ScrapeCompany)

