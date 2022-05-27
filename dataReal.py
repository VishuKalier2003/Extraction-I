from bs4 import BeautifulSoup
import requests

#Response 200 means that the site responded successfully
#Response 404 means the url is invalid
job_page = requests.get('http://timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
with open('http://timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=') as jobpage:
    soup = BeautifulSoup(jobpage, 'lxml')
    job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
    print(job)
#Beautiful Soup Instance created
soup1 = BeautifulSoup(job_page, 'lxml')
#Finding job
jobs = soup1.find('li', class_='clearfix job-bx wht-shd-bx')
print(jobs)
#Finding company within a job for particular
company = jobs.find('h3', class_='joblist-comp-name')
print(company)
# Finding the skillset required for the particular job
skill_set = jobs.find('span', class_='srp-skills')
print(skill_set)