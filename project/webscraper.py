import bs4
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


def get_companies(content):
  companies = []
  for div in content.find_all(name="div", attrs={"class":"row"}):
      company = div.find_all(name="span", attrs={"class":"company"})
      if len(company) > 0:
        for c in company:
          companies.append(c.text.strip())
      else:
        second_try = div.find_all(name="span", attrs={"class":"result-link-source"})
        for span in second_try:
          companies.append(span.text.strip())
  return(companies)

def get_locations(content):
  locations = []
  spans = content.findAll('span', attrs={'class': 'location'})
  for span in spans:
    locations.append(span.text)
  return(locations)

def get_summary(content):
  summaries = []
  spans = content.findAll('span', attrs={'class':'summary'})
  for span in spans:
    summaries.append(span.text.strip())
  return(summaries)

print(get_summary(content))
