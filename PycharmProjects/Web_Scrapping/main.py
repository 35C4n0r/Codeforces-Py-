from bs4 import BeautifulSoup
import requests
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
tags = soup.find_all('h2')
for job in tags:
    print(job.text)