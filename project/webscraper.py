from bs4 import BeautifulSoup
import requests

url = "https://ca.indeed.com/jobs?q=software+developer&l=Toronto"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


def get_job_titles(content):
  jobs = []
  for div in content.find_all(name="div", attrs={"class":"row"}):
      for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
        jobs.append(a["title"])
  return(jobs)

print(get_job_titles(content))
