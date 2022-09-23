#Quelquews fonctions permettant de faciliter les taches de
#Scrapping
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

class ScrapSite:

    def __init__(self) :
        pass
    
    #fonction permettant de d'analyser et resortir la balise qu'on desire 
    def scanSite(self, url: str, balise: str ):
        self.site = urlopen(url)
        self.site = self.site.read().decode("utf-8")
        
        self.soup = BeautifulSoup(self.site, "html.parser")
        self.findBalises = self.soup.find(balise)
        if self.findBalises == None:
            print("Balise introuvable")
        else:
            print(self.findBalises)
            print("taille: ", len(self.findBalises))
            return self.findBalises
        

    def recupdata(self, data):
        if data is None: 
            print("aucune valeur trouver")
        else:
            self.dataToString = [data.string]
            print(self.dataToString)
            return self.dataToString