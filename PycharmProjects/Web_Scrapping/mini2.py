from bs4 import BeautifulSoup
import requests
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.find_all("div", class_="card")
for job in jobs:
    location = jobs
    print(job.h2.text, job.p.text)