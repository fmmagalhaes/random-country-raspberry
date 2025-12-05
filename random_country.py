# https://restcountries.com/
import random
import requests

BASE_URL = "https://restcountries.com/v3.1"

# Cache for country codes
_country_codes = None


class Country:
    def __str__(self):
        return "{}".format(self.name)

    def __init__(self, country_data):
        capital = country_data.get("capital")
        self.code = country_data.get("cca3")
        self.name = country_data.get("name").get("common")
        self.continent = country_data.get("continents")[0]
        self.population = country_data.get("population")
        self.capital = capital[0] if capital and len(capital) > 0 else None


"""api wrappers"""


def get_country(country_code):
    response = requests.get(f"{BASE_URL}/alpha/{country_code}?fields=name,cca3,capital,continents,population")
    country_data = response.json()

    return Country(country_data)


def get_all_country_codes():
    global _country_codes
    if _country_codes is None:
        response = requests.get(f"{BASE_URL}/all?fields=cca3")
        _country_codes = [country["cca3"] for country in response.json()]
    return _country_codes


def get_random_country():
    country_codes = get_all_country_codes()
    random_code = random.choice(country_codes)

    return get_country(random_code)


def human_format(num):
    """
    number formatter
    https://stackoverflow.com/questions/579310/formatting-long-numbers-as-strings-in-python
    """
    num = float('{:.2g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{} {}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
