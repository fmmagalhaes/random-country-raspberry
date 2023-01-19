# https://github.com/the-raspberry-pi-guy/lcd
import drivers
import requests
import time
import schedule
from random_country import get_random_country, human_format

display = drivers.Lcd()


def display_country_info(country):
    values = [
        country.name,
        country.continent,
        country.capital,
        human_format(country.population)
    ]
    line = 1
    for v in values:
        print(v)
        if v:
            display.lcd_display_string(v, line)
            line += 1


def display_random_country_info():
    country = get_random_country()
    display.lcd_clear()
    display_country_info(country)
    print("----------------")


def safe_display_random_country_info():
    retries = 0
    while retries < 10:
        try:
            display_random_country_info()
            return
        except (requests.ConnectionError, requests.Timeout):
            print("Couldn't get response.")
            print("----------------")

        retries += 1
        time.sleep(5)

    display.lcd_display_string("Failed to connect.", 1)


try:
    safe_display_random_country_info()

    schedule.every().day.at("08:00").do(safe_display_random_country_info)

    while True:
        schedule.run_pending()
        time.sleep(1800)  # 30 minutes

except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
