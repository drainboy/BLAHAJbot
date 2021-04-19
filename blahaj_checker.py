import json
import requests
import re
import blahaj_manual_check
from blahaj_class import Blahaj

def get_blahaj_details(site, country_code):
    if re.search("\w{2}\/\w{2}\/",site):
        try:
            country_lang = re.search("\/[a-z]{2}\/[a-z]{2}\/", site)[0]
            request = requests.get(f"https://sik.search.blue.cdtapps.com{country_lang}search-box?q=blahaj")
            blahaj_details = json.loads(request.content)
            return(blahaj_details["searchBox"]["universal"][0]["product"])
        except (KeyError, IndexError, TypeError):
            return blahaj_manual_check.check(site, country_code)
    else:
        return blahaj_manual_check.check(site, country_code)


def details_to_class(details):
    if type(details) != Blahaj:
        name = details["name"]
        desc = details["typeName"]
        image = details["mainImageUrl"]
        price = float(details["priceNumeral"])
        width = details["itemMeasureReferenceText"]
        link = details["pipUrl"]
        country = ""
        currency_code = details["currencyCode"]
        online_availability = details["onlineSellable"]
        return Blahaj(name, desc, image, price, width, link, country, currency_code, online_availability)
    return details

