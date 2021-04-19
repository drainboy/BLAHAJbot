class Blahaj():
    "Common base class for all BLAHAJ"

    def __init__(self, name, desc, image, price, width, product_link, country, currency_code, online_availabilty):
        self.name = name
        self.desc = desc
        self.image = image
        self.price = price
        self.width = width
        self.link = product_link
        self.country = country
        self.currency_code = currency_code
        self.online_availability = online_availabilty


    def __str__(self):
        return f"{self.name = }\n{self.price = }\n{self.width = }\n{self.link = }\n{self.country = }\n{self.currency_code = }"