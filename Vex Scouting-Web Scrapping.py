#

from bs4 import BeautifulSoup
import urllib.request
def search(team):
  url = "https://vexdb.io/teams/view/"+team
  page = urllib.request.urlopen(url)
  soup = BeautifulSoup(page, 'html.parser')
  information = soup.find_all("td")
  return information

def driverSkills(team):
  return "Driver Skills Score:", search(team)[23]
def progSkills(team):
  return "Programing Skills Score: ",search(team)[25]
def totalEvents(team):
  return "Total Events Attended: ",search(team)[9]
def ranking(team):
  return "Overall Rankings: ", search(team)[15]
print(progSkills("7405K"))
