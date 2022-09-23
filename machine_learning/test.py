from utils import ScrapSite

scrapping = ScrapSite()
scrap = scrapping.scanSite("https://fr.wikipedia.org/wiki/Donald_Trump", "title")

recup = scrapping.recupdata(scrap)