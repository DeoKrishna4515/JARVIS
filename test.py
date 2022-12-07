from plyer import notification  #pip install plyer
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
url = "https://www.cricbuzz.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
div = soup.find_all(class_ = "cb-pos-rel")[0]

try:
    result = div.find(class_= "cb-ovr-flo cb-text-live").text
except:
    result = div.find(class_= "cb-ovr-flo cb-text-complete").text
team1 = div.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
team2 = div.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
team1_score = div.find_all(class_ = "cb-ovr-flo")[2].get_text()
team2_score = div.find_all(class_ = "cb-ovr-flo")[4].get_text()

print(f"In the match of {team1} v/s {team2}: {result}")
print(f"{team1} : {team1_score}")
print(f"{team2} : {team2_score}")

notification.notify(
    app_icon = "C:\\Users\\kravi\\Downloads\\ipl-logo.ico",
    title = f"{team1} v/s {team2}",
    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
    timeout = 15
)