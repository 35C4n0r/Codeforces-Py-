from bs4 import BeautifulSoup
import requests
URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", "").strip()
    skills_required = job.find('span', class_="srp-skills").text.replace(" ", "").strip()
    print(company_name)
    print(skills_required)
    print('')
