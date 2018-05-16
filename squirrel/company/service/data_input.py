# from bs4 import BeautifulSoup
# import requests as rq
#
# from company.models import ScrapeCompany
#
#
# def import_value():
#     google_res = rq.get('http://www.dream71.com/top-10-software-company-in-bangladesh')
#
#     content = google_res.content
#
#     d = {}
#
#     soup = BeautifulSoup(content, 'html.parser')
#
#     position = soup.find('h4', {'class': "job-title"})
#     company_name = soup.find('h2', {'class': "company-name "})
#
#     d = {
#         "name": company_name.text,
#         "position": position.text
#     }
#
#     ScrapeCompany.objects.create(**d)
#     print(d)
#
# # print(all_a_tags.text)
