import time
from get_random_country import get_random_country, human_format

def print_random_country_info(country):
    print(country.name)
    print(country.continent)
    print(country.capital)
    print(human_format(country.population))

try:
    while True:
        country = get_random_country()
        print_random_country_info(country)
        print("----------------")
        time.sleep(1)
except KeyboardInterrupt:
    print("Bye!")
