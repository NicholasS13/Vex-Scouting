#7,266-current num of teams
from bs4 import BeautifulSoup
import urllib.request

team = "750B"
url = "https://vexdb.io/teams/view/"+team
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
info = []
#functions for cmd
def search(look):
    information = soup.find_all("td")
    info = []
    counter = 0
    count = []
    for entries in information:
        if look in entries.getText():
            count.append(counter)
        info.append(entries.getText())
        counter+=1
        return info[count[0]+" "+info[count[0]+1]]

def Ranking(team):
    return team

def Skills(team):
    return "Programming Skills :2 \nDriver :3"

print(search("Total Events"))
#   test = info[1]
