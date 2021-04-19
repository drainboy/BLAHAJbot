import requests
import json
from blahaj_class import Blahaj


def get_blahaj_details(site, country_code):
    request = requests.get(f"{site}products/589/10373589.json")
    if request.status_code != 200:
        request = requests.get(f"{site}products/588/30373588.json")
        if request.status_code != 200:
            request = requests.get(f"{site}products/590/90373590.json")
            if request.status_code != 200:
                return False

    try:
        blahaj_details = json.loads(request.content)

        headers = {"x-client-id":"b6c117e5-ae61-4ef5-b4cc-e0b1e37f0631"}
        avail_link = f"https://api.ingka.ikea.com/cia/availabilities/ru/{country_code.lower()}?itemNos={blahaj_details['id']}&expand=StoresList,Restocks"
    except (KeyError, json.decoder.JSONDecodeError):
        return False

    blahaj_availability = json.loads(requests.get(avail_link, headers=headers).content)
    return (blahaj_details,blahaj_availability)


def details_to_class(details):
    name = details[0]["name"]
    desc = details[0]["typeName"]
    image = details[0]["mainImage"]["url"]
    price = float(details[0]["priceNumeral"])
    width = details[0]["mainImage"]["alt"].split(",")[-1]
    link = details[0]["pipUrl"]
    country = ""
    currency_symbol = details[0]["revampPrice"]["currencySymbol"]
    online_availability = [details[1]["data"]]
    return Blahaj(name, desc, image, price, width, link, country, currency_symbol, online_availability)