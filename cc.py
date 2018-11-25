import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import time


cotes = {
    "id":"",
    "1": "",
    "N": "",
    "2": "",
    "time": ""
}

liste_cotes = ["1", "N", "2"]
compteur_global = 0

while 1:

    today = time.localtime()
    heures = today.tm_hour
    minutes = today.tm_min

    url = 'https://www.winamax.fr/paris-sportifs/match/live/16218996'


    browser = webdriver.PhantomJS()
    browser.get(url)
    htmlSource = browser.page_source

    soup = BeautifulSoup(htmlSource, "lxml")
    compteur = 0
    for ligne in soup.find_all('div',attrs={"class":u"gSzbQZ"}, limit=1): #Récupération lignes impaires
        with open("ligne.html", "w", encoding="UTF-8") as fichier:
            fichier.write(str(ligne))

        for lala in ligne.find_all('div', attrs={"class":u"cdEkMQ"}, limit=3):
            cotes[liste_cotes[compteur]] = lala.text
            compteur = compteur + 1

    cotes["time"] = str(heures)+"h"+str(minutes)
    cotes["id"] = str(compteur_global)
    compteur_global = compteur_global + 1

    with open('bdd_variation_cotes.json', 'a') as outfile:
        json.dump(cotes, outfile, indent=4, ensure_ascii=False)

    print("Pause de 60 secondes")
    time.sleep(60)
