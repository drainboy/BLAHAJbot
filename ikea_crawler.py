import pycountry
from bs4 import BeautifulSoup
import requests
import json


country_list = [country.alpha_2 for country in pycountry.countries]


def crawl_ikea(country_alpha_2):
    ikea_site = requests.get(f"https://www.ikea.com/{country_alpha_2}")
    if ikea_site.status_code == 200:
        country = pycountry.countries.get(alpha_2=country_alpha_2)
        if ikea_site.url[-1] != "/":
            ikea_site.url += "/"
        return (ikea_site.url,{"country": country.name, "country_code": country_alpha_2})


def create_ikea_json():
    ikea_sites = {}
    for code in country_list:
        if crawl := crawl_ikea(code):
            ikea_site, country = crawl   
            ikea_sites[ikea_site] = country
    with open("ikea_sites.json","w") as ikea:
        ikea.write(json.dumps(ikea_sites, indent=4))
    

def load_ikea_json():
    with open("ikea_sites.json") as ikea_sites:
        return json.load(ikea_sites)

if __name__ == "__main__":
    create_ikea_json()
