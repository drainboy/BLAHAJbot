import ikea_crawler
import blahaj_checker
import discord_bot

BLAHAJ = []


def update_ikea_json():
    ikea_crawler.create_ikea_json()


def init():
    for ikea in (ikea_dict := ikea_crawler.load_ikea_json()):
        country_code = ikea_dict[ikea]["country_code"]
        if details := blahaj_checker.get_blahaj_details(ikea, country_code):
            blahaj = blahaj_checker.details_to_class(details)
            blahaj.country = ikea_dict[ikea]
            BLAHAJ.append(blahaj)


def main():
    init()
    discord_bot.run_bot(BLAHAJ)
    

if __name__ == "__main__":
    main()