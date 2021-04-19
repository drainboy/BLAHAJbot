from discord.ext import commands
import discord
import pycountry
import os
from stay_awake import stay_awake


TOKEN = os.environ['DISCORD_TOKEN']


def run_bot(blahaj_list):
    bot = commands.Bot(command_prefix="!")

    @bot.command(name="blahaj", help="Shows you the price of a country's IKEA BLÅHAJ")
    async def blahaj(ctx, *country: str):
        country = " ".join(country).lower()
        desc_msg = f"{country.capitalize()} doesn't have BLÅHAJ😢"

        try :
            pycountry.countries.search_fuzzy(country)
        except LookupError:
            desc_msg = f"Given country ({country}) isn't a country🤔"

        embedVar = discord.Embed(title="Error 404", description=desc_msg, color=0xff0033)

        for haj in blahaj_list:
            if country in haj.country["country"].lower():
                embedVar = embed(haj)
        
        await ctx.send(embed=embedVar)

    @bot.command(name="countries_avail", help="Shows you all countries that BLÅHAJbot understands")
    async def countries_avail(ctx):
        message = "I spotted a **BLÅHAJ** here:\n"
        avail_countries = "\n".join([blahaj.country["country"] for blahaj in blahaj_list])
        await ctx.send(message + avail_countries)

    stay_awake()
    bot.run(TOKEN)


def embed(haj):
    embedVar = discord.Embed(title=haj.name, description=haj.desc, color=0x0058a3, url=haj.link)
    embedVar.set_thumbnail(url=haj.image)
    embedVar.add_field(name="Width", value=haj.width, inline=True)
    embedVar.add_field(name="Country", value=haj.country["country"], inline=True)
    embedVar.add_field(name="Price", value=f"{haj.price} {haj.currency_code}", inline=False)
    embedVar.add_field(name=f"Availability", value=boolean_convertion(haj.online_availability,"✅","⛔"), inline=False)
    embedVar.set_footer(text="brought to you by blahajgang🦈 & melonsquad🍉",icon_url="https://melon.blahajgang.lol/Assets/BLAHAJ.gif")
    return embedVar


def boolean_convertion(boolean, if_true, if_false):
    if boolean:
        return if_true
    elif boolean is None:
        return "❔"
    return if_false