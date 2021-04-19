from bs4 import BeautifulSoup
from blahaj_class import Blahaj
import blahaj_checker2
import requests


def check(site, country_code):
    if country_code == "TR":
        request = requests.get(f"https://www.ikea.com.tr/arama/?k=blahaj")
        soup = BeautifulSoup(request.content, "html.parser")

        product_link = site + soup.find("div", class_="product-bottom").a["href"]
        product_req = requests.get(product_link)
        product_soup = BeautifulSoup(product_req.content, "html.parser")

        product_title = product_soup.find("h1", class_="product-title")
        name = product_title.a.text
        desc = product_title.span.text.strip()

        price_div = product_soup.find("div", class_="price")
        price = float(price_div.span.text.strip()[:-1])
        symbol = price_div.span.text.strip()[-1]

        image = "https:" + product_soup.find("div", class_="item").a["href"]

        width = product_soup.find("div", class_="product-info-content").p.text.split(":")[1]

        return Blahaj(name, desc, image, price, width, product_link, "Turkey", symbol, None)
    elif country_code == "CY":
        request = requests.get(f"{site}apotelesmata-anazitisis/?query=blahaj")
        soup = BeautifulSoup(request.content, "html.parser")
        

    elif country_code in ["BH", "EG"]:
        return blahaj_checker2.details_to_class(blahaj_checker2.get_blahaj_details(site,country_code))
    else:
        print(country_code)
        return False