from utils import ScrapSite

scrapping = ScrapSite()
scrap = scrapping.scanSite("https://www.socolas-blog.com/parler-senegal-vocabulaire-wolof-diola-peul/", "td")

recup = scrapping.recupData(scrap)